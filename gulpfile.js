const gulp = require('gulp');
const path = require('path');
const exec = require('child_process').exec;

const change_require = basename => {
  const suffix = basename === 'requirements.in' ? 'dep' : 'devDep';
  console.log(`docker-compose exec ap sh/pip-install ${suffix}`);
  exec(`docker-compose exec ap sh/pip-install ${suffix}`, (err, stdout, stderr) => {
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
        change_require(basename);
      }
      if (basename === 'docker-compose.yml' ||
          basename === 'ap') {
        console.log('docker-compose up -d ap');
        exec('docker-compose up -d ap', (err, stdout, stderr) => {
          stdout && console.log(`stdout: ${stdout}`);
          stderr && console.log(`stderr: ${stderr}`);
          err && console.log(`err: ${err}`);
        });
      }
    }
  });
});

gulp.task('default', ['watch-docker']);
