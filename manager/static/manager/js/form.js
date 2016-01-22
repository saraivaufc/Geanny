var options = {
		onSelect: function() {
			$(".geanny-form-field-date").each(function() {
				$(this).get(0).MaterialTextfield.checkDirty();
				$(this).get(0).MaterialTextfield.checkDisabled();
				$(this).get(0).MaterialTextfield.checkValidity();
			});
		}, 
		dateFormat: "dd/mm/yy"
};

componentHandler.registerUpgradedCallback("MaterialLayout", function(elem) {
	
	if($(".geanny-form-field").get(0) != undefined) {
		$(".geanny-form-field").get(0).MaterialTextfield.checkDirty();
		$(".geanny-form-field").get(0).MaterialTextfield.checkDisabled();
		$(".geanny-form-field").get(0).MaterialTextfield.checkValidity();
	}
	
	$(".geanny-form-field-password").addClass("is-dirty");
	
	$('.geanny-form-field-date-input').datepicker(options);
	
	$(".geanny-file-input-field").each(function() {
		$field = $(this);
		
		$field.find(".geanny-file-input-field-hidden").change(function() {
			$field.find(".geanny-file-input-field-input").val(
					$field.find(".geanny-file-input-field-hidden").val());
			$field.find(".geanny-file-input-field-text").get(0).MaterialTextfield.checkDirty();
		});
		
		$field.find(".geanny-file-input-field-button").click(function() {
			$field.find(".geanny-file-input-field-hidden").click()
		});
	});
		
});

