var editor = CKEDITOR.replace( 'editor1' );
Array.prototype.secondLast = function() {
    return this[this.length-2];
}
// The "change" event is fired whenever a change is made in the editor.
editor.on( 'change', function( evt ) {
    // getData() returns CKEditor's HTML content.

    if(CKEDITOR.instances.editor1.document.getBody().getText().slice(-1) == ".")
    {
        $.post( "http://localhost:5000", { line: CKEDITOR.instances.editor1.document.getBody().getText().split(".").secondLast()})
          .done(function( data ) {
            alert( "Data Loaded: " + data );
          });
    }
});
