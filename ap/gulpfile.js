const gulp = require('gulp');
const path = require('path');
const exec = require('child_process').exec;

const echoExec = (cmd, cb) => {
  console.log('==========');
  console.log(`+ ${cmd}`);
  console.log('==========');
  exec(cmd, cb);
};


const relativePath = p => path.relative(__dirname, p);

const watchPyDocker = serviceName => () => {
  gulp.watch([
    path.join(serviceName, 'requirements.in'),
    path.join(serviceName, 'requirements.dev.in'),
    path.join(serviceName, 'docker-compose.yml'),
    path.join(serviceName, 'env_file', serviceName),
  ], event => {
    if (event.type == 'added' || event.type == 'changed') {
      const targetPath = relativePath(event.path);
      const basename = path.basename(event.path);

      if (targetPath === path.join(serviceName, 'requirements.in') ||
          targetPath === path.join(serviceName, 'requirements.dev.in')) {
        echoExec(`docker-compose -f ${path.join(serviceName, 'docker-compose.yml')} exec ${serviceName} /docker_bin/pip-install ${basename}`, (err, stdout, stderr) => {
          stdout && console.log(`stdout: ${stdout}`);
          stderr && console.log(`stderr: ${stderr}`);
          err && console.log(`err: ${err}`);
        });
      } else if (targetPath === path.join(serviceName, 'docker-compose.yml') ||
          targetPath === path.join(serviceName, 'env_file', serviceName)) {
        echoExec(`docker-compose -f ${path.join(serviceName, 'docker-compose.yml')} up -d ${serviceName}`, (err, stdout, stderr) => {
          stdout && console.log(`stdout: ${stdout}`);
          stderr && console.log(`stderr: ${stderr}`);
          err && console.log(`err: ${err}`);
        });
      }
    }
  });
};

const serviceNames = ['ap', 'fabric'];
serviceNames.forEach(s => gulp.task(`watch.docker.${s}`, watchPyDocker(s)));

gulp.task('default', ['watch.docker.ap']);
