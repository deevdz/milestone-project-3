// Code for Search Overlay
$(document).ready(function() {
    $('#close-btn').click(function() {
        $('#search-overlay').fadeOut();
        $('#search-btn').show();
    });
    $('#search-btn').click(function() {
        $(this).hide();
        $('#search-overlay').fadeIn();
    });
});

 // Materialize Code
  $(document).ready(function() {
    $('select').material_select();
    $(".button-collapse").sideNav();
  });         


// Code for Adding and Removing Ingredients and Steps on Add Recipe Page
var ingredient_field = '<div class="row new-ingredient"> <div class="input-field col s10 m11"><input type="text" name="recipe_ingredients" class="validate" required><label>Ingredient(s)</label></div><div class="col s2 m1"><a class="btn-floating waves-effect waves-light" id="remove_ingredient"> <i class="material-icons">remove</i></a></div></div>';
var step_field =   '<div class="row new-method-step"> <div class="input-field col s10 m11"><input type="text" name="recipe_method" class="validate" required><label>Step</label></div><div class="col s2 m1"><a class="btn-floating waves-effect waves-light" id="remove_method_step"> <i class="material-icons">remove</i></a></div></div>'; 

// Add Ingredient to Recipe
$("#add_ingredient").click(function() {
    $("#ingredients").append(ingredient_field);
    Materialize.updateTextFields();
});
// Remove the Ingredient from Recipe
$("body").on("click","#remove_ingredient", function() {
    $(this).parents(".new-ingredient").remove();
});

// Add Step to Recipe Method
$("#add_method_step").click(function() {
    $("#steps").append(step_field);
    Materialize.updateTextFields();
});

// Remove the Ingredient from Recipe
$("body").on("click","#remove_method_step", function() {
   $(this).parents(".new-method-step").remove();
}); 

//Code to bind chip input to hidden input field
     function updateChipInput(chip){
       var newval= $(chip).material_chip('data')
          .reduce(function(result,val){ result.push(val.tag); return result;},[]).join(",")
  
       $('input[name="recipe_tags"]').val(newval);
     }
    
    $(document).ready(function(){
     var data= $('input[name="recipe_tags"]').val().split(',') 
       .map(function(tag){
         return {tag:tag}
       })
    
     $('.chips').material_chip({
       data: data,
      autocompleteData: {
       'Apple': "x",
       'Microsoft': "u",
       'Google': "y"
      }   
    });
    
     $('.chips').on('chip.add', function(e, chip){
       updateChipInput(this);
    })
     .on('chip.delete', function(e, chip){
       updateChipInput(this);
    });  
   });
   
   
 // Code for Homepage Slider
var slideIndex = 0;
showSlides();

function showSlides() {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}
  slides[slideIndex-1].style.display = "block";
  setTimeout(showSlides, 5000); // Change image every 2 seconds
}