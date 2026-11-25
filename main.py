import os

LINE = "deploy: Friday's last check passed after I removed the one check that knew prod"

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
path = os.path.join(output_dir, "entry.txt")
expected = LINE.encode("utf-8")

with open(path, "wb") as entry:
    entry.write(expected)

os.chmod(path, 0o644)

with open(path, "rb") as entry:
    if entry.read() != expected:
        raise IOError("entry.txt did not match the requested text")

print(len(LINE))
