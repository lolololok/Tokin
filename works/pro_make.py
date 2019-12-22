import subprocess


def python_make(file_path):
    res = subprocess.Popen(
        f"python {file_path}",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    std_out = res.stdout.read()
    std_err = res.stderr.read()
    return (std_out + std_err).decode("gbk")


