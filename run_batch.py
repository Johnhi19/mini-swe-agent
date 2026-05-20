import subprocess
from datetime import datetime

pandas_prs = {
    # '55108': '0bdbc44babac09225bdde02b642252ce054723e3',
    # '57034': 'd928a5cc222be5968b2f1f8a5f8d02977a8d6c2d',
    # '57399': '719e4a638a4383b859d684db4ad4f7e471a58aaa',
    # '60538': '5c9b6718dea589be6fafab04adbd22dd0550a061',
    #'61966': 'c849d39c4c956495c0c86b85ab561bf74bf5df8d',
    '61054': '0490e1b27cdbf7f5fbed8f6bf37300419b6f3490',
    '60828': '0e245de0bd1b71f903bb16a03ff45fc6d7625946',
    '61946': '1d2233185083423b8ecb27986f11175b2d6e8fa6'
}

scipy_prs = {
    # '19263': '92fe79409b2a463c0e589b3e3e27ac11d337613a',
    # '20751': '0ab0e563e67c06122a9fe055e619c5f442900537',
    # '20974': '055ea4532f2a15c68ac0db6786af005933bd0b87',
    # '21076': '5247c04bc9fbd0c4834d443d410bf9e9a0e1d5d7',
    # '21768': 'ea916c6f7f487bd53e98de082649d542cc6106ed',
    '23341': '87b1d46a1fac6b90c731326ce0cae07bcbbceb08',
    '22213': '776fe38d9fd9bbb6d001ddd56ea2b9d55c43991a'
}

marshmallow_prs = {
    '2800': '76bc28ae74e723760d54f097290ba85e717d5fe4',
    '2698': 'f6393c378403042904b7c4d7cad34925fe31132c'
}

keras_prs = {
    #'20974': '21c8997e3a758cfa9a8dfbf3868a59006faf895e',
    '20765': 'cc467763c84589fec2e08f21475815f0b4c25bb6',
    '20626': 'aab9458ed43de7b117ece0e563a630afe72cb5db'
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
    run_batch('scipy', scipy_prs, 'scipy.yaml')
    #run_batch('marshmallow', marshmallow_prs, 'marshmallow.yaml')
    # run_batch('keras', keras_prs, 'keras.yaml')