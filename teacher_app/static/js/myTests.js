let sortingOrder = "ASC"
let sortedBy = "time"
WritingRecords = get_sorting_order(WritingRecords, 'DESC', 'checkedQuestion')
add_writing_records(WritingRecords, $("#recordWritingShow"))

function getCurrentFormattedDate(dateTime) {
    const months = [
        "JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE",
        "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"
    ];

    const dateObj = new Date(dateTime);

    const day = dateObj.getDate();
    const month = months[dateObj.getMonth()];
    const year = dateObj.getFullYear();

    let hour = dateObj.getHours();
    const minute = dateObj.getMinutes();
    const ampm = hour >= 12 ? "PM" : "AM";

    // Convert to 12-hour clock format
    if (hour > 12) {
        hour -= 12;
    } else if (hour === 0) {
        hour = 12;
    }

    return `${day}-${month}-${year} ${hour}:${minute.toString().padStart(2, '0')} ${ampm}`;
}

function add_writing_records(records, recordTable) {
    //records = JSON.parse(records)
    //$("#recordWritingShow").empty();
    console.log(recordTable);
    recordTable.empty();
    for (var i = 0; i < records.length; i++) {
        var inputTr = "<tr class=''><td>" + (Number(i) + 1) + "</td><td>" + getCurrentFormattedDate(records[i].timestamp) + "</td><td>" + records[i].teacher.username + "</td><td>" + records[i].teacher.email + "</td>";
        if (records[i].checkedQuestion) {
            inputTr += "<td><span class='badge rounded-pill bg-success'>Checked</span></td><td>" + records[i].studentObtainMarks + "</td></tr>"
        }
        else {
            inputTr += "<td><span class='badge rounded-pill bg-secondary'>Not Checked</span></td><td>" + records[i].studentObtainMarks + "</td></tr>"
        }

        //$("#recordWritingShow").append(inputTr);
        recordTable.append(inputTr);
        console.log(inputTr);
    }
}

//click listners
$("#time").click(function () {
    var $icon = $('#time').find('i');
    if ($icon.attr('class') == 'fas fa-angle-down' || $icon.attr('class') == 'fa-angle-down fas') {
        sortingOrder = 'ASC'
        $icon.removeClass('fas fa-angle-down').addClass('fas fa-angle-up');
    }
    else {
        sortingOrder = 'DESC'
        $icon.removeClass('fas fa-angle-up').addClass('fas fa-angle-down');
    }
    records = get_sorting_order(WritingRecords, sortingOrder, 'time')
    add_writing_records(records, $("#recordWritingShow"))
    $("#status i, #marks i").removeClass('fas fa-angle-up').addClass('fas fa-angle-down');
});
$("#status").click(function () {
    var $icon = $('#status').find('i');
    if ($icon.attr('class') == 'fas fa-angle-down' || $icon.attr('class') == 'fa-angle-down fas') {
        records = get_sorting_order(WritingRecords, 'ASC', 'status')
        $icon.removeClass('fas fa-angle-down').addClass('fas fa-angle-up');
    }
    else {
        records = get_sorting_order(WritingRecords, 'DESC', 'status')
        $icon.removeClass('fas fa-angle-up').addClass('fas fa-angle-down');
    }
    add_writing_records(records, $("#recordWritingShow"))
    $("#time i, #marks i").removeClass('fas fa-angle-up').addClass('fas fa-angle-down');

});
$('#marks').click(function () {
    var $icon = $('#marks').find('i');
    if ($icon.attr('class') == 'fas fa-angle-down' || $icon.attr('class') == 'fa-angle-down fas') {
        records = get_sorting_order(WritingRecords, 'ASC', 'marks')
        $icon.removeClass('fas fa-angle-down').addClass('fas fa-angle-up');
    }
    else {
        records = get_sorting_order(WritingRecords, 'DESC', 'marks')
        $icon.removeClass('fas fa-angle-up').addClass('fas fa-angle-down');
    }
    add_writing_records(records, $("#recordWritingShow"))
    $("#time i, #status i").removeClass('fas fa-angle-up').addClass('fas fa-angle-down');

});

//sorting function

function get_sorting_order(records, sortingOrder = 'ASC', sortedBy = 'time') {
    if (sortingOrder == 'ASC') {
        if (sortedBy == 'time') {
            records.sort(function (a, b) {
                return new Date(a.timestamp) - new Date(b.timestamp);
            });
        }
        else if (sortedBy == 'marks') {
            records.sort(function (a, b) {
                return a.studentObtainMarks - b.studentObtainMarks;
            });
        }
        //else if (sortedBy == 'status') {
        //        records.sort(function (a, b) {
        //        return a.status - b.status;
        //    });                    
        //}

    }
    else {
        if (sortedBy == 'time') {
            records.sort(function (a, b) {
                return new Date(b.timestamp) - new Date(a.timestamp);
            });
        }
        else if (sortedBy == 'marks') {
            records.sort(function (a, b) {
                return b.studentObtainMarks - a.studentObtainMarks;
            });
        }
        else if (sortedBy == 'status') {
            records.sort(function (a, b) {
                return b.checkedQuestion - a.checkedQuestion;
            });
        }
    }
    return records;
}



