$(document).ready(function () {
  $(document).on('click', '.deleteConfirm', function() {
    return confirm("確定提交訂單?提交後將不能夠在更改訂單");
  });
});