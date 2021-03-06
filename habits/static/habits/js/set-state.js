// Set state of habit
$( document ).ready(function() {
    console.log( "ready!" );
    $('.section-icon-bottom-toggle').on('touchstart', function() {
      console.log(active_habit_id.habit);
      // alert('Hello Baby!');
      console.log('toggleBtn is fired!');
      var setActive;
      var habitWhichChangeID = active_habit_id.habit;
      // console.log(document.getElementById('section-icon-bottom-toggle_' + id).firstChild.nextElementSibling.classList[1]);
      if (document.getElementById('section-icon-bottom-toggle_' + habitWhichChangeID).firstChild.nextElementSibling.classList[1] == 'fa-toggle-off') {
        console.log('Habit wird aktiviert!');
        setActive = true;
          document.getElementById('habit_' + habitWhichChangeID).classList.remove('non-sortable');
      } else {
        console.log('Habit wird deaktiviert');
        setActive = false;
        listItem  =   document.getElementById('habit_' + habitWhichChangeID);
        // alert(listItem);
        listItem.className += 'non-sortable';
        console.log(listItem);
      }

      for (var i = 0; i < sessionStorage.length; i++) {
        var acc = 'accordion_' + habitWhichChangeID;

        if (sessionStorage.key(i) == acc) {
          var csrftoken = getCookie('csrftoken');

         //This is the Ajax post.Observe carefully. It is nothing but details of where_to_post,what_to_post

          $.ajax({
                  url : "/overview/habit/state/", // the endpoint,commonly same url
                  type : "POST", // http method
                  data : { csrfmiddlewaretoken : csrftoken,
                      habit_id : habitWhichChangeID,
                      state : setActive

          }, // data sent with the post request

          // handle a successful response
          success : function(json) {
             console.log(json); // another sanity check
             sessionStorage.removeItem('accordion_' + json['habitWhichChangeID']);
             console.log(sessionStorage);
             window.location.href = "/overview/";

          },

          // handle a non-successful response
          error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
          }
          });
        }
      }
    });
  });
