  document.addEventListener('DOMContentLoaded', function() {
    // initialises the side nav bar
    let sidenavbar = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenavbar);
  });

  document.addEventListener('DOMContentLoaded', function() {
    // initialises the carousel to display park records on home page
    let parkDisplay = document.querySelectorAll('.carousel');
    M.Carousel.init(parkDisplay, {
      indicators: true,
      dist: -20,
      shift: 30,
      duration: 150,
    });
  });

  document.addEventListener('DOMContentLoaded', function() {
    // initialises the date picker for date_opened on the add_park form 
    let dateOpened = document.querySelectorAll('.datepicker');
    M.Datepicker.init(dateOpened, {
      yearRange: 50,
    });
  });
  
  document.addEventListener('DOMContentLoaded', function() {
    // initialises the time picker for time_open & time_closed on the add_park form
    let openingTimes = document.querySelectorAll('.timepicker');
    M.Timepicker.init(openingTimes, {
      format: 'HH-mm', // changing format of how time is displayed
    });
  });

  document.addEventListener('DOMContentLoaded', function() {
    // initialises textual hint for card reveal on parks cards
    let parkCard = document.querySelectorAll('.tooltipped');
    M.Tooltip.init(parkCard);
  });

  document.addEventListener('DOMContentLoaded', function() {
    // initialises modal to confirm whether user is sure to delete the record
    let deleteModal = document.querySelectorAll('.modal');
    M.Modal.init(deleteModal, {
      opacity: 0.8,
    });
  });

  document.addEventListener('DOMContentLoaded', function() {
    // initialises tabs on ride and restaurant records
    let cardTabs = document.querySelectorAll('.tabs');
    M.Tabs.init(cardTabs);
});

document.addEventListener('DOMContentLoaded', function() {
  // initialises drop down list of parks on forms
  let parkList = document.querySelectorAll('select');
  M.FormSelect.init(parkList);
});

document.querySelectorAll('.fa-xmark').forEach(function(elem) {
  // Manually initialising close of card reveal on parks records
  elem.addEventListener('click', function() {
    elem.closest('.card-reveal').style.display = 'none';
  });
});

