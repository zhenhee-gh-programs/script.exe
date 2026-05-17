\[ "script.exe" , Windows OS Crash Simulation ]



⚠️ **CRITICAL WARNING: DANGEROUS CODE** ⚠️

This repository contains code designed to force-terminate system processes (svchost.exe) and flood system resources. Running this script will cause an  system crash (Blue Screen of Death) and system instability. 



**\*\*DO NOT RUN THIS CODE ON YOUR PRIMARY COMPUTER.\*\*** 

It should only ever be executed inside a completely isolated Virtual Machine (VM) sandbox environment. The author is not responsible for any data loss, hardware damage, or system corruption.



⚠️ **NOTICE:** ⚠️

I am **not responsible** for any **damage done to your computer**. Run this program at **your own risk**. If you accidently open the program, open Task Manager and kill the program **immediately**.







🔬 Educational Purpose \& Intent



This project is hosted strictly for educational, security research, and dual-use software analysis purposes under GitHub's Acceptable Use Policies. 

The objective of this script is to demonstrate:

1\. The critical dependency of the Windows OS on core infrastructure processes like svchost.exe.

2\. How rapid file-system calls (Denial of Service) can deplete CPU and RAM resources.



No pre-compiled executable (.exe) is provided in this repository to prevent unauthorized execution or malicious deployment.





🛠️ How to Safely Analyze or Test



To view or test this script, you must manually execute the Python source code in a safe sandbox environment:



1\. Set up an Isolated VM : Deploy a clean instance of Windows inside a Virtual Machine (e.g., VirtualBox or VMware).

2\. Install Python: Ensure Python 3.x is installed inside the guest VM.

3\. Download the Script : Copy the raw text of scipt.py into the VM.

4\. Open Terminal as Admin : Open PowerShell or Command Prompt as an Administrator inside the VM.

4\. Run the Script : Navigate to your folder and open the program using commands.





📜 License \& Compliance



This project is intended as an open-source educational resource. It does not contain any delivery mechanisms, obfuscation tactics, or exploit delivery payloads. If you plan to fork this repository, you must maintain these strict safety disclaimers.



