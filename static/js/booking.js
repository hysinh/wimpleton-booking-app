const venueSelection = document.getElementById("venue").addEventListener("change", getCapacity);

/* Object of Venue and correspondeing guest capacities */
let venues = [
  {name: "The Chapel", capacity: 150},
  {name: "The Mansion Formal Rooms", capacity: 200},
  {name: "The Conservatory", capacity: 175}
];


/* Gets the venue capacity based on the Venue selected for a booking request BACKUP */
function getCapacity() {
  console.log("inside the function");
}

/* Gets the venue capacity based on the Venue selected for a booking request BACKUP */
// function getCapacity() {
//   console.log("inside the function");
//   /* updates the upper limited for capacity*/
//   let selectedVenue = document.getElementById("guests");
//   let capacity = document.getElementById("capacity");
//   let venueOptions = document.querySelectorAll(".selected-venue");


//   console.log(selectedVenue.max, capacity.innerText);
//   console.log('VenueOptions node: ', venueOptions[0].value);

//   for (let venue of venueOptions) {
//     console.log('Selected values for class selected-venue: ', venue.value);


    // if (venueId.value === venue) {
      
    //   console.log("Finally in the for loop");
    //   console.log(venue);
    //   console.log(venues[venue]);
    //   console.log(selectedVenue.max);
    //   selectedVenue.max = venues[venue];
    //   capacity.innerText = venues[venue];
    //   console.log('updated max capacity: ', selectedVenue.max);
    // }
//   }

//   for (let x of venues) {
//     console.log('venue keys: ', x);
//   }


//   console.log("Event attributes: ", selectedVenue.max);
// }




