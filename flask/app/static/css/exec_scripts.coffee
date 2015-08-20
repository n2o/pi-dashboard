$ ->
  $(".execute").click ->
    $("#execution").hide()
    $("#loading").show()

    script = $(this).context.title

    $.getJSON '/_exec', {
      script: script
    }, (data) ->
      $("#loading").hide()
      $("#execution").show()

      if data.out.length > 3
        $("#output-wrapper").show()
        $("#output").html data.out

      if data.err.length > 3
        $("#error-wrapper").show()
        $("#error").html data.err
