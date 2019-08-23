$( "form" ).submit(function( event ) {  
  if ( $( "input:first" ).val() === "javatpoint" ) {  
    $( "span" ).text( "Submitted Successfully." ).show();  
    return;  
  }  

    <div class="alert alert-danger p-5 hidden" id="timer">0</div>
      <button id="startButton">Start</button>
      <button id="resetButton">Reset</button>

      <script>
        $('#searchform').on('submit', function(e) {
          alert("Submitted"); 
        })

        var i = 1;
        $("#startButton").click(function (e) {
          setInterval(function () {
            $("#timer").html(i);
            i++;
          }, 1000);
        });
      

      $("#resetButton").click(function (e) {
        i = 0;
      });