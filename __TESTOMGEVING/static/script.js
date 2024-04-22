function moveToNext(current, event) {
    if (current.value.length >= current.maxLength) {
        var form = current.form;
        for (var i = 0; i < form.elements.length; i++) {
            if (form.elements[i] == current) {
                if (form.elements[i + 1]) {
                    form.elements[i + 1].focus();
                }
                return;
            }
        }
    }
}
