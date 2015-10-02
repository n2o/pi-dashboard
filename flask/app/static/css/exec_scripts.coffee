icon_spinner = "<i class='fa fa-refresh fa-spin'>"
icon_play = "<i class='fa fa-play'>"


$ ->
  $(".execute").click ->
    # Hide content and show loading div
    $(".execute").prop "disabled", true

    button = $(this)
    button.context.innerHTML = icon_spinner
    change_process_label "warning"

    # Get script name with extension
    script = $(this).context.title

    url = "/stream/" + script
    $("#execute").attr "src", url


change_process_label = (status) ->
  if status == "success"
    $("#process_label")[0].innerHTML = "<span class='label label-success'>Bereit</span>"
  else if status == "warning"
    $("#process_label")[0].innerHTML = "<span class='label label-warning'>Wird ausgeführt</span>"
  else if status == "danger"
    $("#process_label")[0].innerHTML = "<span class='label label-danger'>Fehler</span>"


window.stream_success = ->
  ### This function is triggered when the streaming process has successfully finished ###
  buttons = $(".execute")
  buttons.prop "disabled", false
  for button in buttons
    do ->
      button.innerHTML = icon_play
  change_process_label "success"


window.stream_error = ->
  ### This function is triggered when the streaming process threw an error ###
  buttons = $(".execute")
  buttons.prop "disabled", false
  for button in buttons
    do ->
      button.innerHTML = icon_play
  change_process_label "danger"