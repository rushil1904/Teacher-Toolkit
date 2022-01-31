let {PythonShell} = require('python-shell')
var path = require("path")


function get_weather() {

  // var city = document.getElementById("city").value
  
  // const { dialog } = require('electron').remote;
	//   	dialog.showOpenDialog((fileNames) => {
	//     if (fileNames === undefined) {
	//       return;
	//     }
	//     document.getElementById("city").value = fileNames[0]
	//     // document.getElementById("filename").innerHTML = fileNames[0]

	//   });
  
  const { dialog } = require('electron').remote;
  let options = {
    // See place holder 1 in above image
    // title : "Custom title bar", 
    
    // See place holder 2 in above image
    // defaultPath : "D:\\electron-app",
    
    // See place holder 3 in above image
    // buttonLabel : "Custom button",
    
    // See place holder 4 in above image
    // filters :[
    //  {name: 'Images', extensions: ['jpg', 'png', 'gif']},
    //  {name: 'Movies', extensions: ['mkv', 'avi', 'mp4']},
    //  {name: 'Custom File Type', extensions: ['as']},
    //  {name: 'All Files', extensions: ['*']}
    // ],
    // properties: ['openFile','multiSelections']
    properties:["openDirectory"]
   }
	//  dialog.showOpenDialog(options, (dirs) => {
  //   if (dirs === undefined) {
  //           return;
  //         }
  //   document.getElementById("city").value  = dirs[0]
  //  });
  let dirs = dialog.showOpenDialog(options)
  document.getElementById("city").value  = dirs[0]
  // var dir_path = 'F:\Rashmi_mam\sample_pdf';
  var resource_path = path.join(__dirname, '/../fonts/')
  console.log(resource_path)
  var options_pythonshell = {
      scriptPath : path.join(__dirname, '/../engine/'),
      args : [dirs[0], resource_path]
  };
  console.log(resource_path)
  
  // let pyshell = new PythonShell('teacher_toolkit.py', options_pythonshell);
  
  var python = require("child_process").execFile("teacher_toolkit", [dirs[0],resource_path]);
  // PythonShell.run('teacher_toolkit.py', options);
  console.log(resource_path)
    // pyshell.on('message', function(message) {
    //   swal(message);
    // })
    // document.getElementById("city").value = "";

  //   python.stderr.on("data", (data) => {
  //     console.error(`stderr: ${data}`);
  //     console.log(`stderr: ${data}`);
  // });
}
