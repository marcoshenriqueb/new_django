var gulp = require('gulp');
var stylus = require('gulp-stylus');
var browserify = require('gulp-browserify');

gulp.task('stylus', function () {
  gulp.src('./resources/stylus/site.styl')
    .pipe(stylus())
    .pipe(gulp.dest('./sitefront/static/sitefront/css'));
});

gulp.task('script', function() {
	// Single entry point to browserify
	gulp.src('./resources/js/app.js')
		.pipe(browserify({
		  insertGlobals : true
		}))
		.pipe(gulp.dest('./sitefront/static/sitefront/js'))
});

gulp.task('watch', function() {
  gulp.watch('./resources/stylus/site.styl', ['stylus']);
  gulp.watch('./resources/js/app.js', ['script']);
});
