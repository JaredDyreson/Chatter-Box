function insert(ch) {
    s = document.form.field1.value
    if (s.length > 0) {
        document.form.field1.value = s + " " + ch
    }
    else {
        document.form.field1.value = ch
    }
}


function enter() {
    var exp = document.form.field1.value;
    document.form.field2.value = exp;
    document.form.field1.value = 3;
}

function allClear() {
    document.form.field2.value = document.form.field1.value = ""
    }

function del() {
    var s = document.form.field1.value
    var n = s.length
    if (n > 1) {
        while (s[n-1] != " ") {
            n--;
        }
        document.form.field1.value = s.slice(0, n-1);    
    }
    else {
        allClear();
    }
}

