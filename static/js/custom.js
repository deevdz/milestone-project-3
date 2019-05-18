// Code for Search Overlay
var search_screen = document.getElementById('search-overlay');

$(document).ready(function() {
    $('#search-btn').click(function() {
        $(this).hide();
        $('#search-overlay').fadeIn();
    });
});

window.onclick = function(event) {
    if (event.target == search_screen) {
        search_screen.style.display = 'none';
        $('#search-btn').show();
    }
};

 // Materialize Code
$(document).ready(function() {
    $('.button-collapse').sideNav();
    $('select').material_select();
 });  
  
$('.button-collapse').sideNav({
      closeOnClick: true, // Closes side-nav on <a> clicks, useful for Angular/Meteor
});  

// Code for Adding and Removing Ingredients and Steps on Add Recipe Paget
var ingredient_field = '<div class="new-ingredient"><div class="input-field col s11"><input placeholder="Ingredients" type="text" name="recipe_ingredients" class="validate" required></div><div class="col s1"><a class="btn-floating waves-effect waves-light" id="remove_ingredient"> <i class="material-icons">remove</i></a></div></div>';
var step_field =   '<div class="new-method-step"><div class="input-field col s11"><input placeholder="Steps" type="text" name="recipe_method" class="validate" required></div><div class="col s1"><a class="btn-floating waves-effect waves-light" id="remove_method_step"> <i class="material-icons">remove</i></a></div></div>'; 

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