$ ->
  $(".execute").click ->
    # Hide content and show loading div
    # $(".execute").prop "disabled", true
    # $("#execution").hide()
    # $("#loading").show()

    $(".execute").removeClass "btn-danger"
    $(".execute").removeClass "btn-success"

    icon_spinner = "<i class='fa fa-refresh fa-spin'>"
    icon_play = "<i class='fa fa-play'>"
    button = $(this)

    # Get script name with extension
    script = $(this).context.title

    button.context.innerHTML = icon_spinner

    url = "/stream/" + script
    $("#execute").attr "src", url


    # Make AJAX request
    ###$.getJSON '/_exec', {
      script: script
    }, (data) ->
      $(".execute").prop "disabled", false    # Reactivate the buttons

      $("#loading").hide()                    # Toggle divs
      $("#execution").show()

      # Show output if available
      if data.out.length > 3
        button.addClass "btn-success"
        button.removeClass "btn-danger"
        $("#output-wrapper").show()
        $("#output").html data.out

      if data.err.length > 3
        button.removeClass "btn-success"
        button.addClass "btn-danger"
        $("#error-wrapper").show()
        $("#error").html data.err

      # Make again play icon for button
      button.context.innerHTML = icon_play###