var gulp = require('gulp');
var sass = require('gulp-sass');
var autoprefixer = require('gulp-autoprefixer');

var sassPaths = [
  'node_modules/foundation-sites/scss',
];
gulp.task('sass', function () {
  return gulp.src('static_src/scss/app.scss')
    .pipe(sass({
      includePaths: sassPaths
    })
    .on('error', sass.logError))
    .pipe(autoprefixer({
      browsers: ['last 2 versions'],
      cascade: false
    }))
    .pipe(gulp.dest('static/css'));
});

gulp.task('sass:watch', function () {
  gulp.watch('static_src/scss/**/*.scss', ['sass']);
});

gulp.task("build", ["sass"]);
