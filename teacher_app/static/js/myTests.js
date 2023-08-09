let sortingOrder = "ASC"
let sortedBy = "time"

WritingRecords = get_sorting_order(WritingRecords, 'DESC', 'checkedQuestion')
add_writing_records(WritingRecords, $("#recordWritingShow"))

listeningTestData = get_sorting_order(listeningTestData, 'DESC', 'checkedQuestion')
add_writing_records(listeningTestData, $("#recordShowListening"))

readingTestData = get_sorting_order(readingTestData, 'DESC', 'checkedQuestion')
add_rading_records(readingTestData, $("#recordShowReading"))

speakingTestData = get_sorting_order(speakingTestData, 'DESC', 'checkedQuestion')
add_writing_records(speakingTestData, $("#recordShowSpeaking"))

///////////////////////
/// command methods ///
///////////////////////
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
    recordTable.empty();
    for (var i = 0; i < records.length; i++) {
        var inputTr = "<tr class=''><td>" + (Number(i) + 1) + "</td><td>" + getCurrentFormattedDate(records[i].timestamp) + "</td><td>" + records[i].teacher.username + "</td><td>" + records[i].teacher.email + "</td>";
        if (records[i].checkedQuestion) {
            inputTr += "<td><span class='badge rounded-pill bg-success'>Checked</span></td><td>" + records[i].studentObtainMarks + "</td><td><a class='btn btn-success'>view</a></td></tr>"
        }
        else {
            inputTr += "<td><span class='badge rounded-pill bg-secondary'>Not Checked</span></td><td>" + records[i].studentObtainMarks + "</td><td><a class='btn btn-success'>view</a></td></tr>"
        }

        //$("#recordWritingShow").append(inputTr);
        recordTable.append(inputTr);
    }
}
function add_rading_records(records, recordTable) {
    //records = JSON.parse(records)
    //$("#recordWritingShow").empty();
    recordTable.empty();
    for (var i = 0; i < records.length; i++) {
        var inputTr = "<tr class=''><td>" + (Number(i) + 1) + "</td><td>" + getCurrentFormattedDate(records[i].testNumber.submitTime) + "</td><td>" + records[i].teacher.username + "</td><td>" + records[i].teacher.email + "</td>";
        if (records[i].checkedQuestion) {
            inputTr += "<td><span class='badge rounded-pill bg-success'>Checked</span></td><td>" + records[i].studentObtainMarks + "</td></tr>"
        }
        else {
            inputTr += "<td><span class='badge rounded-pill bg-secondary'>Not Checked</span></td><td>" + records[i].studentObtainMarks + "</td><td><a class='btn btn-success'>view</a></td></tr>"
        }

        //$("#recordWritingShow").append(inputTr);
        recordTable.append(inputTr);
    }
}

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
        else if (sortedBy == 'status') {
            records.sort(function (a, b) {
                return a.status - b.status;
            });
        }

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
///////////////////////////////
/// writing click listeners ///
///////////////////////////////

$("#timeWriting").click(function () {
    var $icon = $('#timeWriting').find('i');
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
    $("#statusWriting i, #marksWriting i").removeClass('fas fa-angle-up').addClass('fas fa-angle-down');
});
$("#statusWriting").click(function () {
    var $icon = $('#statusWriting').find('i');
    if ($icon.attr('class') == 'fas fa-angle-down' || $icon.attr('class') == 'fa-angle-down fas') {
        records = get_sorting_order(WritingRecords, 'ASC', 'status')
        $icon.removeClass('fas fa-angle-down').addClass('fas fa-angle-up');
    }
    else {
        records = get_sorting_order(WritingRecords, 'DESC', 'status')
        $icon.removeClass('fas fa-angle-up').addClass('fas fa-angle-down');
    }
    add_writing_records(records, $("#recordWritingShow"))
    $("#timeWriting i, #marksWriting i").removeClass('fas fa-angle-up').addClass('fas fa-angle-down');

});
$('#marksWriting').click(function () {
    var $icon = $('#marksWriting').find('i');
    if ($icon.attr('class') == 'fas fa-angle-down' || $icon.attr('class') == 'fa-angle-down fas') {
        records = get_sorting_order(WritingRecords, 'ASC', 'marks')
        $icon.removeClass('fas fa-angle-down').addClass('fas fa-angle-up');
    }
    else {
        records = get_sorting_order(WritingRecords, 'DESC', 'marks')
        $icon.removeClass('fas fa-angle-up').addClass('fas fa-angle-down');
    }
    add_writing_records(records, $("#recordWritingShow"))
    $("#timeWriting i, #statusWriting i").removeClass('fas fa-angle-up').addClass('fas fa-angle-down');

});

/////////////////////////////////
/// Listening click listeners ///
/////////////////////////////////

$("#timeListening").click(function () {
    var $icon = $('#timeListening').find('i');
    if ($icon.attr('class') == 'fas fa-angle-down' || $icon.attr('class') == 'fa-angle-down fas') {
        sortingOrder = 'ASC'
        $icon.removeClass('fas fa-angle-down').addClass('fas fa-angle-up');
    }
    else {
        sortingOrder = 'DESC'
        $icon.removeClass('fas fa-angle-up').addClass('fas fa-angle-down');
    }
    records = get_sorting_order(listeningTestData, sortingOrder, 'time')
    add_writing_records(records, $("#recordShowListening"))
    $("#statusListening i, #marksListening i").removeClass('fas fa-angle-up').addClass('fas fa-angle-down');
})

$("#statusListening").click(function () {
    var $icon = $('#statusListening').find('i');
    if ($icon.attr('class') == 'fas fa-angle-down' || $icon.attr('class') == 'fa-angle-down fas') {
        records = get_sorting_order(listeningTestData, 'ASC', 'status')
        $icon.removeClass('fas fa-angle-down').addClass('fas fa-angle-up');
    }
    else {
        records = get_sorting_order(listeningTestData, 'DESC', 'status')
        $icon.removeClass('fas fa-angle-up').addClass('fas fa-angle-down');
    }
    add_writing_records(records, $("#recordShowListening"))
    $("#timeListening i, #marksListening i").removeClass('fas fa-angle-up').addClass('fas fa-angle-down');
})

$("#marksListening").click(function () {
    var $icon = $('#marksListening').find('i');
    if ($icon.attr('class') == 'fas fa-angle-down' || $icon.attr('class') == 'fa-angle-down fas') {
        records = get_sorting_order(listeningTestData, 'ASC', 'marks')
        $icon.removeClass('fas fa-angle-down').addClass('fas fa-angle-up');
    }
    else {
        records = get_sorting_order(listeningTestData, 'DESC', 'marks')
        $icon.removeClass('fas fa-angle-up').addClass('fas fa-angle-down');
    }
    add_writing_records(records, $("#recordShowListening"))
    $("#timeListening i, #statusListening i").removeClass('fas fa-angle-up').addClass('fas fa-angle-down');
});

/////////////////////////////////
/// Reading click listeners /////
/////////////////////////////////


$("#timeReading").click(function () {
    var $icon = $('#timeReading').find('i');
    if ($icon.attr('class') == 'fas fa-angle-down' || $icon.attr('class') == 'fa-angle-down fas') {
        sortingOrder = 'ASC'
        $icon.removeClass('fas fa-angle-down').addClass('fas fa-angle-up');
    }
    else {
        sortingOrder = 'DESC'
        $icon.removeClass('fas fa-angle-up').addClass('fas fa-angle-down');
    }
    records = get_sorting_order(readingTestData, sortingOrder, 'time')
    add_rading_records(records, $("#recordShowReading"))
    $("#statusReading i, #marksReading i").removeClass('fas fa-angle-up').addClass('fas fa-angle-down');
});

$("#statusReading").click(function () {
    var $icon = $('#statusReading').find('i');
    if ($icon.attr('class') == 'fas fa-angle-down' || $icon.attr('class') == 'fa-angle-down fas') {
        records = get_sorting_order(readingTestData, 'ASC', 'status')
        $icon.removeClass('fas fa-angle-down').addClass('fas fa-angle-up');
    }
    else {
        records = get_sorting_order(readingTestData, 'DESC', 'status')
        $icon.removeClass('fas fa-angle-up').addClass('fas fa-angle-down');
    }
    add_rading_records(records, $("#recordShowReading"))
    $("#timeReading i, #marksReading i").removeClass('fas fa-angle-up').addClass('fas fa-angle-down');
});

$("#marksReading").click(function () {
    var $icon = $('#marksReading').find('i');
    if ($icon.attr('class') == 'fas fa-angle-down' || $icon.attr('class') == 'fa-angle-down fas') {
        records = get_sorting_order(readingTestData, 'ASC', 'marks')
        $icon.removeClass('fas fa-angle-down').addClass('fas fa-angle-up');
    }
    else {
        records = get_sorting_order(readingTestData, 'DESC', 'marks')
        $icon.removeClass('fas fa-angle-up').addClass('fas fa-angle-down');
    }
    add_rading_records(records, $("#recordShowReading"))
    $("#timeReading i, #statusReading i").removeClass('fas fa-angle-up').addClass('fas fa-angle-down');
});

/////////////////////////////////
/// Speaking click listeners ////
/////////////////////////////////


$("#timeSpeaking").click(function () {
    var $icon = $('#timeSpeaking').find('i');
    if ($icon.attr('class') == 'fas fa-angle-down' || $icon.attr('class') == 'fa-angle-down fas') {
        sortingOrder = 'ASC'
        $icon.removeClass('fas fa-angle-down').addClass('fas fa-angle-up');
    }
    else {
        sortingOrder = 'DESC'
        $icon.removeClass('fas fa-angle-up').addClass('fas fa-angle-down');
    }
    records = get_sorting_order(speakingTestData, sortingOrder, 'time')
    add_writing_records(records, $("#recordShowSpeaking"))
    $("#statusSpeaking i, #marksSpeaking i").removeClass('fas fa-angle-up').addClass('fas fa-angle-down');
});

$("#statusSpeaking").click(function () {
    var $icon = $('#statusSpeaking').find('i');
    if ($icon.attr('class') == 'fas fa-angle-down' || $icon.attr('class') == 'fa-angle-down fas') {
        records = get_sorting_order(speakingTestData, 'ASC', 'status')
        $icon.removeClass('fas fa-angle-down').addClass('fas fa-angle-up');
    }
    else {
        records = get_sorting_order(speakingTestData, 'DESC', 'status')
        $icon.removeClass('fas fa-angle-up').addClass('fas fa-angle-down');
    }
    add_writing_records(records, $("#recordShowSpeaking"))
    $("#timeSpeaking i, #marksSpeaking i").removeClass('fas fa-angle-up').addClass('fas fa-angle-down');
});

$("#marksSpeaking").click(function () {
    var $icon = $('#marksSpeaking').find('i');
    if ($icon.attr('class') == 'fas fa-angle-down' || $icon.attr('class') == 'fa-angle-down fas') {
        records = get_sorting_order(speakingTestData, 'ASC', 'marks')
        $icon.removeClass('fas fa-angle-down').addClass('fas fa-angle-up');
    }
    else {
        records = get_sorting_order(speakingTestData, 'DESC', 'marks')
        $icon.removeClass('fas fa-angle-up').addClass('fas fa-angle-down');
    }
    add_writing_records(records, $("#recordShowSpeaking"))
    $("#timeSpeaking i, #statusSpeaking i").removeClass('fas fa-angle-up').addClass('fas fa-angle-down');
});






