var gulp = require('gulp');
var stylus = require('gulp-stylus');
var browserify = require('browserify');
var vueify = require('vueify');
var source = require('vinyl-source-stream');


gulp.task('stylus', function () {
  gulp.src('./resources/stylus/site.styl')
    .pipe(stylus())
    .pipe(gulp.dest('./sitefront/static/sitefront/css'));
});

gulp.task('script', function() {
  browserify('./resources/js/app.js')
  .transform(vueify)
  .bundle()
  .pipe(source('app.bundled.js'))
  .pipe(gulp.dest('./sitefront/static/sitefront/js'));
});

gulp.task('watch', function() {
  gulp.watch('./resources/stylus/site.styl', ['stylus']);
  gulp.watch('./resources/js/app.js', ['script']);
});
