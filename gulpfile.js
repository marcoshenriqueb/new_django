var gulp = require('gulp');
var stylus = require('gulp-stylus');
var browserify = require('browserify');
var vueify = require('vueify');
var source = require('vinyl-source-stream');
var imagemin = require('gulp-imagemin');
var pngquant = require('imagemin-pngquant');
var imageResize = require('gulp-image-resize');
var rename = require('gulp-rename');


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
  gulp.watch('./resources/stylus/**/*.styl', ['stylus']);
  gulp.watch('./resources/js/**/*', ['script']);
});

gulp.task('image', function() {
    return gulp.src('./resources/images/*.jpg')
        .pipe(imageResize({
            width : 1200,
            crop : false,
            upscale : false,
            ImageMagick: true
        }))
        .pipe(imagemin({
            progressive: true,
            svgoPlugins: [{removeViewBox: false}],
            use: [pngquant()]
        }))
        .pipe(rename({suffix: "-md"}))
        .pipe(gulp.dest('./sitefront/static/sitefront/images'))
        .pipe(imageResize({
            width : 800,
            crop : false,
            upscale : false,
            ImageMagick: true
        }))
        .pipe(imagemin({
            progressive: true,
            svgoPlugins: [{removeViewBox: false}],
            use: [pngquant()]
        }))
        .pipe(rename(function (path) {
            var l = path.basename.length - 3;
            path.basename = path.basename.substr(0, l);
            path.basename += "-sm";
          }))
        .pipe(gulp.dest('./sitefront/static/sitefront/images'));
});
