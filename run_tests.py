import subprocess

cmd_list = ["docker", "run", "-d", "--name", "testing", "-w", 
            "/home/testing", "-v", "/home/hierlinger/mini-swe-agent/input:/home/mini-swe-agent/input",
            "mini-swe-custom-scipy", "sleep", "2h"]

subprocess.run(cmd_list, capture_output=True, check=True)

print("Container started")

cmd_test_before_patch = ["docker", "exec", "testing", "python" "-c", "import scipy; scipy.__version__; scipy.test()"]

try:
    # We use capture_output to see the version and test results
    result = subprocess.run(cmd_test_before_patch, capture_output=True, check=True, text=True)
    print("Output:\n", result.stdout)
except subprocess.CalledProcessError as e:
    print("Error during execution:\n", e.stderr)


