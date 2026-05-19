import subprocess
from datetime import datetime

pandas_prs = {
    '55108': '0bdbc44babac09225bdde02b642252ce054723e3',
    '57034': 'd928a5cc222be5968b2f1f8a5f8d02977a8d6c2d',
    '57399': '719e4a638a4383b859d684db4ad4f7e471a58aaa',
    '60538': '5c9b6718dea589be6fafab04adbd22dd0550a061'
}

scipy_prs = {
    '19263': '92fe79409b2a463c0e589b3e3e27ac11d337613a',
    # '20751': '0ab0e563e67c06122a9fe055e619c5f442900537',
    # '20974': '055ea4532f2a15c68ac0db6786af005933bd0b87',
    # '21076': '5247c04bc9fbd0c4834d443d410bf9e9a0e1d5d7',
    # '21768': 'ea916c6f7f487bd53e98de082649d542cc6106ed'
}

marshmallow_prs = {
    '2800': '76bc28ae74e723760d54f097290ba85e717d5fe4',
    '2698': 'f6393c378403042904b7c4d7cad34925fe31132c'
}

def run_batch(project: str, prs: dict, config_file: str = 'default.yaml'):

    for pr_nr, target_commit in prs.items():

        task = f"""
First run the script in `/home/mini-swe-agent/input/rebuild_{project}.sh {target_commit}` to trigger the rebuild of the correct {project} version. IMPORTANT: Run it ONLY ONCE as a single command.

Please solve the issue found in /home/mini-swe-agent/input/issues/{project}_{pr_nr}.txt

Assume that {project} is installed in an editable mode at the correct version for the PR. The source code is stored under /home/{project}, if you want to look at it.

write the patch into /home/mini-swe-agent/input/patches/{project}_{pr_nr}.diff with 'git diff' so we can apply that patch later with 'git apply'
""" 
        
        cmd_list = [
            "timeout", "40m", 
            "mini", "-c", config_file,
            "-y", "--task", task
        ]

        start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(f"agent_logs/agent_log_{project}_{pr_nr}.txt", "w") as f:

            f.write(f"======= Agent Started At: {start_time} =======\n")

            process = subprocess.Popen(cmd_list, stdout=f, stderr=f)

        print(f"Started mini-swe-agent for PR_NR: {pr_nr} in background with PID: {process.pid} at {start_time}")


if __name__ == "__main__":

    #run_batch('pandas', pandas_prs)
    #run_batch('scipy', scipy_prs, 'scipy.yaml')
    run_batch('marshmallow', marshmallow_prs, 'marshmallow.yaml')