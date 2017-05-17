const gulp = require('gulp');
const path = require('path');
const exec = require('child_process').exec;

const echo_exec = (cmd, cb) => {
  console.log(cmd);
  exec(cmd, cb);
};


const change_require = basename => {
  echo_exec(`docker-compose exec ap docker_bin/pip-install ${suffix}`, (err, stdout, stderr) => {
    stdout && console.log(`stdout: ${stdout}`);
    stderr && console.log(`stderr: ${stderr}`);
    err && console.log(`err: ${err}`);
  });
};


gulp.task('watch-docker', () => {
  gulp.watch([
    'requirements.in', 'requirements.dev.in', 'docker-compose.yml',
    'env_files/ap'
  ], event => {
    if (event.type == 'added' || event.type == 'changed') {
      const basename = path.basename(event.path);
      if (basename === 'requirements.in' ||
          basename === 'requirements.dev.in') {

        echo_exec(`docker-compose exec ap docker_bin/pip-install ${basename}`, (err, stdout, stderr) => {
          stdout && console.log(`stdout: ${stdout}`);
          stderr && console.log(`stderr: ${stderr}`);
          err && console.log(`err: ${err}`);
        });
      }
      if (basename === 'docker-compose.yml' ||
          basename === 'ap') {
        echo_exec('docker-compose up -d ap', (err, stdout, stderr) => {
          stdout && console.log(`stdout: ${stdout}`);
          stderr && console.log(`stderr: ${stderr}`);
          err && console.log(`err: ${err}`);
        });
      }
    }
  });
});

gulp.task('default', ['watch-docker']);
