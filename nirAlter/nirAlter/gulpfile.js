// including plugins
    var gulp      = require('gulp');
        less      = require("gulp-less"),
        minifycss = require('gulp-minify-css'),
        rename    = require('gulp-rename'),
        plumber   = require('gulp-plumber'),

    // Task - Compile less
    gulp.task('compile-less', function () {
      gulp.src('static/less/bootstrap/bootstrap.less')
      .pipe(plumber())
      .pipe(less())
      .pipe(gulp.dest('static/css'))
      .pipe(rename({suffix: '.min'}))
      .pipe(minifycss())
      .pipe(gulp.dest('static/css'));
    });

    // Task - watch for changes
    gulp.task('watch-less', function () {
       gulp.watch('static/less/bootstrap/**/*.less', ['compile-less']);
       gulp.watch('static/less/bootstrap/*.less', ['compile-less']);
    });

    // Task - 'Gulp' Command in terminal
    gulp.task('default', ['compile-less', 'watch-less'],
        function () {
    });
