from flask import Flask, render_template, request, redirect, url_for
import os
import subprocess
import shutil
import time


filename = 'inputfile'
app = Flask(__name__)

try:
   os.remove('/app/inputfile.txt')
   os.remove('/app/ymlgenerator/inputfile.txt')
except FileNotFoundError:
    print(f"File {file_path} does not exist.")
except Exception as e:
    print(f"An error occurred while deleting the file: {e}")


#os.remove('/app/inputfile.txt')
#os.remove('/app/ymlgenerator/inputfile.txt')

time.sleep(1)

f = open("/app/inputfile.txt", "w")
f = open("/app/ymlgenerator/inputfile.txt", "w")

src_dir = '/app/inputfile.txt' 
dest_dir = '/app/ymlgenerator/inputfile.txt'

@app.route('/home')
def message():
    return render_template('home.html')

@app.route('/buttons')
def buttons():
    return render_template('buttons.html')


@app.route('/script')
def script_execution():
    script_output = ""
    script_errors = ""



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/save', methods=['POST'])
def save():
    Hostname = request.form.get('Hostname')
    BMC_IP = request.form.get('content')
   # serverkind = request.form.get('serverkind')
    RobinVerison = request.form.get('dropdown1')
    Host_IP = request.form.get('Host_IP')
   # date = request.form.get('date')
    RCP_Version = request.form.get('dropdown2')
    ServerKind = request.form.get('dropdown4')
    B_vlan = request.form.get('B_vlan')
   # S_Type = request.form.get('S_Type')
    S_Type = request.form.get('dropdown3')
    OS_profile = request.form.get('dropdown5')

    if filename and BMC_IP and Host_IP and RCP_Version and ServerKind and RobinVerison and B_vlan and S_Type:
        file_content = f"{Hostname}\n{RCP_Version}\n{BMC_IP}\n{Host_IP}\n{ServerKind}\n{RobinVerison}\n{B_vlan}\n{S_Type}\n{OS_profile}"

        with open(f'{filename}.txt', 'w') as file:
            file.write(file_content)
        
        shutil.copyfile(src_dir,dest_dir)
        try:
            os.chdir('/app/ymlgenerator/')
            #subprocess.run(["python3", "myscript.py"], check=True)
            result = subprocess.run(["sh", "ymlgenerate.sh"], capture_output=True, text=True)
            #os.system(./home/kube/flaskapp/ymlgenerator/ymlgenerate.sh)
            script_output = result.stdout
            script_errors = result.stderr
            os.chdir('/app')
        except Exception as e:
            script_errors = str(e)
           
    return render_template('script.html', script_output=script_output, script_errors=script_errors)

           # success_message = "File created successfully."
            # os.chdir('/app')
            #time.sleep(10)
           # return redirect(url_for('success', message=success_message))
       # except Exception as e:
           # error_message = f"Error: {str(e)}"
           # return redirect(url_for('error', message=error_message))
    #else:
     #   return "Please provide all required information."

@app.route('/success')
def success():
    success_message = request.args.get('message', 'Form submitted successfully.')
    return redirect(url_for('index', message=success_message))
    
    time.sleep(5)

   # return redirect('/')
@app.route('/error')
def error():
    error_message = request.args.get('message', 'An error occurred.')
    return f"{error_message} Redirecting to the index..."

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
