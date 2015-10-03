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
          .done(function( data) {
            alert( "Data Loaded: " + data['line'] + data['score'] );
            var editor = CKEDITOR.instances.editor1,
            selection = editor.getSelection(),
            root = selection.root,
            textNodes = [],
            ranges = [],
            range, text, index;

            function getTextNodes( element ) {
                var children = element.getChildren(),
                    child;

                for ( var i = children.count(); i--; ) {
                    child = children.getItem( i );
                    if ( child.type == CKEDITOR.NODE_ELEMENT )
                        getTextNodes( child );
                    else if ( child.type == CKEDITOR.NODE_TEXT )
                        textNodes.push( child );
                }
            }

            // Recursively search for text nodes starting from root.
            // You may want to search a specific branch starting from other element.
            getTextNodes( root );
            for ( i = textNodes.length; i--; )
            {
               text = textNodes[i];
               index = text.getText().trim().indexOf( data['line'].trim() );
               if ( index > -1 ) {
                  range = editor.createRange();
                  range.setStart( text, index );

                  // Note: 3 is fixed length of "the". You may want to change it.
                  range.setEnd( text, index + data['line'].length );
                  ranges.push( range );
               }
            }

            // Select all ranges "containing" phrase "the".
            selection.selectRanges( ranges );

          });
    }
});
