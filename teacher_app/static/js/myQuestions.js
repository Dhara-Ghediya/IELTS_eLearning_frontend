/////////////////////////////////////////
/// commune use function and variables///
/////////////////////////////////////////

const recordsPerPage = 10;

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
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function message_dialog(method, id, msgDialog, recordList, updateTable) {
    return new Promise(function (resolve, reject) {
        Swal.fire({
            icon: 'info',
            iconColor: '#d91818',
            title: msgDialog,
            showCancelButton: true,
            confirmButtonText: 'Delete',
            confirmButtonColor: '#cc2900',
            cancelButtonColor: '#949392',
        }).then((result) => {
            if (result.isConfirmed) {
                method(id)
                    .then((data) => {
                        if (data.msg.status === 'success') {
                            recordList = recordList.filter(function (record) {
                                return record.id !== id;
                            });

                            Swal.fire({
                                icon: 'success',
                                title: 'Success',
                                text: data.msg.msg,
                            });
                            updateTable(recordList, 0);
                            resolve(recordList);
                        } else if (data.msg.status === 'warning') {
                            Swal.fire({
                                icon: 'warning',
                                title: 'Warning',
                                text: data.msg.msg,
                            });
                        } else if (data.msg.status === 'error') {
                            Swal.fire({
                                icon: 'error',
                                title: 'Oops...',
                                text: data.msg.msg,
                            });
                        }
                        return recordList;
                    })
                    .catch((error) => {
                        console.log('Error:', error);
                    });
            }
        });
    });

}

///////////////////////////////////////////////////////
/// declaring records and converting in json format ///
///////////////////////////////////////////////////////

// wiring records declarations
try {
    writingRecords = writingRecords.replace(/None/g, "null");
    writingRecords = writingRecords.replace(/'/g, '"');
    writingRecords = JSON.parse(writingRecords)

} catch (e) {
    writingRecords = [];
    console.log("writingRecords declaration");
    console.log("found error: " + e)
}

//reading records declarations
try {
    readingRecords = readingRecords.replace(/None/g, "null");
    readingRecords = readingRecords.replace(/'/g, '"');
    readingRecords = JSON.parse(readingRecords)
}
catch (e) {
    readingRecords = []
    console.log("readingRecords declaration");
    console.log("found error: " + e)
}
// listening records declarations
try {
    listeningRecords = listeningRecords.replace(/None/g, "null");
    listeningRecords = listeningRecords.replace(/'/g, '"');
    listeningRecords = JSON.parse(listeningRecords)
}
catch (e) {
    listeningRecords = []
    console.log("listeningRecords declaration");
    console.log("found error: " + e)
}

//speaking records declarations
try {
    speakingRecords = speakingRecords.replace(/None/g, "null");
    speakingRecords = speakingRecords.replace(/'/g, '"');
    speakingRecords = JSON.parse(speakingRecords)
}
catch (e) {
    speakingRecords = []
    console.log("speakingRecords declaration");
    console.log("found error: " + e)
}
////////////////////////////
/// add records in table ///
////////////////////////////

function add_writing_records(records, startIndex) {

    let count = startIndex;
    $("#writingQuestionRecordShow").empty();
    for (var i of records) {
        //var inputTr = "<tr class=''><td>" + (Number(i) + 1) + "</td><td>" + getCurrentFormattedDate(records[i].timestamp) + "</td><td>Writing Test</td><td>" + records[i].teacher.username + "</td><td>" + records[i].teacher.email + "</td>";
        var inputTr = `
                    <tr>
                        <td> ` + (Number(count) + 1) + `</td>
                        <td>
                            <p class='text-truncate' style='width: 400px; overflow: hidden; white-space: nowrap; text-overflow: ellipsis;'>` + i.question.question1.content1 + `</p>
                            <p class='text-truncate' style='width: 400px; overflow: hidden; white-space: nowrap; text-overflow: ellipsis;'>` + i.question.question2.content2 + `</p>
                        </td>
                    <td>`
        if (i.question.question1.image != null) {
            inputTr += `
                    <img style='height:50px' src=` + i.question.question1.image + ` class='rounded mx - auto d - block' >`    
        }
        else {
            inputTr += "<img style='height:50px' src='https://png.pngtree.com/png-vector/20190820/ourmid/pngtree-no-image-vector-illustration-isolated-png-image_1694547.jpg' class='rounded mx - auto d - block' >"
        }
        inputTr +=`</td>
        <td>` + getCurrentFormattedDate(i.timeStamp) + `</td>
        <td><a href='#' class='btn rounded btn-primary' style='background-color: #ffc107; border-color: #ffc107;''>Edit</a></td>
        <td><a href='#' class='btn btn-danger rounded'>Delete</a></td>
        <td><a href='#' class='btn btn-success rounded'>Tests</a></td>
    </tr> `
        $("#writingQuestionRecordShow").append(inputTr);

        count++;
    }
}

function add_listening_records(records, startIndex) {
    let count = startIndex;
    $("#listeningQuestionRecordShow").empty();
    for (var i of records) {
        var inputTr = "<tr><td> " + (Number(count) + 1) + "</td><td><audio controls><source src = " + i.question + " ></audio></td><td>" + getCurrentFormattedDate(i.timeStamp) + "</td><td><a href='#' class='btn rounded btn-primary' style='background-color: #ffc107; border-color: #ffc107;''>Edit</a></td><td><a onclick='delete_single_listening_record(" + i.id + ")'  class='btn btn-danger rounded'>Delete</a></td><td><a href='#' class='btn btn-success rounded'>Tests</a></td></tr> "


        $("#listeningQuestionRecordShow").append(inputTr);

        count++;
    }
}

function add_reading_records(records, startIndex) {
    let count = startIndex;
    $("#readingQuestionRecordShow").empty();
    for (var i of records) {
        var inputTr = "<tr><td> " + (Number(count) + 1) + "</td><td><p class='text-truncate' style='width: 400px; overflow: hidden; white - space: nowrap; text - overflow: ellipsis;'>" + i.question + "</td><td class='text-center'>" + i.subQuestion.length + "</td><td>" + getCurrentFormattedDate(i.timeStamp) + "</td><td><a href='#' class='btn rounded btn-primary' style='background-color: #ffc107; border-color: #ffc107;''>Edit</a></td><td><a onclick='delete_single_reading_record(" + i.id + ")' class='btn btn-danger rounded'>Delete</a></td><td><a href='#' class='btn btn-success rounded'>Tests</a></td></tr> "

        $("#readingQuestionRecordShow").append(inputTr);

        count++;
    }
}

function add_speaking_records(records, startIndex) {
    let count = startIndex;
    $("#speakingQuestionRecordShow").empty();
    for (var i of records) {
        var inputTr = "<tr><td> " + (Number(count) + 1) + "</td><td><p class='text-truncate' style='width: 400px; overflow: hidden; white - space: nowrap; text - overflow: ellipsis;'>" + i.question + "</td><td>" + getCurrentFormattedDate(i.timeStamp) + "</td><td><a href='#' class='btn rounded btn-primary' style='background-color: #ffc107; border-color: #ffc107;''>Edit</a></td><td><a onclick='delete_single_speaking_record(" + i.id + ")' class='btn btn-danger rounded'>Delete</a></td><td><a href='#' class='btn btn-success rounded'>Tests</a></td></tr> "

        $("#speakingQuestionRecordShow").append(inputTr);

        count++;
    }

}
/////////////////////////////////////////////////
/// update pagination for show pages in table ///
/////////////////////////////////////////////////

function updatePaginationWriting(currentPage, totalRecords) {
    const totalPages = Math.ceil(totalRecords / recordsPerPage);
    let paginationHtml = '<ul class="pagination justify-content-center">';

    for (let page = 1; page <= totalPages; page++) {
        paginationHtml += `
        <li class="page-item ${page === currentPage ? 'active' : ''}">
          <a class="page-link" href="#" onclick="showPageWriting(${page})">${page}</a>
        </li>
      `;
    }

    paginationHtml += '</ul>';
    $("#writingpagination").html(paginationHtml);
}

function showPageWriting(pageNumber) {
    const startIndex = (pageNumber - 1) * recordsPerPage;
    const endIndex = startIndex + recordsPerPage;
    const recordsToShow = writingRecords.slice(startIndex, endIndex);
    add_writing_records(recordsToShow, startIndex);
    updatePaginationWriting(pageNumber, writingRecords.length);
}
// Initial page load (show the first page)
showPageWriting(1);

// lisning question 
console.log(listeningRecords)
listeningRecords = listeningRecords.replace(/None/g, "null");
listeningRecords = listeningRecords.replace(/'/g, '"');
listeningRecords = JSON.parse(listeningRecords)
function add_listening_records(records, startIndex) {
    let count = startIndex;
    $("#listeningQuestionRecordShow").empty();
    for (var i of records) {
        var inputTr = "<tr><td> " + (Number(count) + 1) + "</td><td><audio controls><source src = " + i.question + " ></audio></td><td>" + getCurrentFormattedDate(i.timeStamp) + "</td><td><a href='#' class='btn rounded btn-primary' style='background-color: #ffc107; border-color: #ffc107;''>Edit</a></td><td><a href='#' class='btn btn-danger rounded'>Delete</a></td><td><a href='#' class='btn btn-success rounded'>Tests</a></td></tr> "


        $("#listeningQuestionRecordShow").append(inputTr);

        count++;
    }
}
function updatePaginationlistening(currentPage, totalRecords) {
    const totalPages = Math.ceil(totalRecords / recordsPerPage);
    let paginationHtml = '<ul class="pagination justify-content-center">';

    for (let page = 1; page <= totalPages; page++) {
        paginationHtml += `
        <li class="page-item ${page === currentPage ? 'active' : ''}">
          <a class="page-link" href="#" onclick="showPageListening(${page})">${page}</a>
        </li>
      `;
    }

    paginationHtml += '</ul>';
    $("#listeningpagination").html(paginationHtml);
}

function updatePaginationReading(currentPage, totalRecords) {
    const totalPages = Math.ceil(totalRecords / recordsPerPage);
    let paginationHtml = '<ul class="pagination justify-content-center">';

    for (let page = 1; page <= totalPages; page++) {
        paginationHtml += `
        <li class="page-item ${page === currentPage ? 'active' : ''}">
        <a class="page-link" href="#" onclick="showPageReading(${page})">${page}</a>
        </li>
        `;
    }

    paginationHtml += '</ul>';
    $("#readingpagination").html(paginationHtml);
}

function updatePaginationSpeaking(currentPage, totalRecords) {
    const totalPages = Math.ceil(totalRecords / 10);
    let paginationHtml = '<ul class="pagination justify-content-center">';

    for (let page = 1; page <= totalPages; page++) {
        paginationHtml += `
        <li class="page-item ${page === currentPage ? 'active' : ''}">
        <a class="page-link" href="#" onclick="showPageSpeaking(${page})">${page}</a>
        </li>
        `;
    }

    paginationHtml += '</ul>';
    $("#speakingPagination").html(paginationHtml);

}
/////////////////////////////////////////////////////////////////
/// show calculating pages and number of records show in page ///
/////////////////////////////////////////////////////////////////

function showPageListening(pageNumber) {
    const startIndex = (pageNumber - 1) * recordsPerPage;
    const endIndex = startIndex + recordsPerPage;
    const recordsToShow = listeningRecords.slice(startIndex, endIndex);
    add_listening_records(recordsToShow, startIndex);
    updatePaginationListening(pageNumber, listeningRecords.length);
}

function showPageReading(pageNumber) {
    const startIndex = (pageNumber - 1) * recordsPerPage;
    const endIndex = startIndex + recordsPerPage;
    const recordsToShow = readingRecords.slice(startIndex, endIndex);
    add_reading_records(recordsToShow, startIndex);
    updatePaginationReading(pageNumber, readingRecords.length);
}

function showPageSpeaking(pageNumber) {
    const startIndex = (pageNumber - 1) * 10;
    const endIndex = startIndex + 10;
    const recordsToShow = speakingRecords.slice(startIndex, endIndex);
    add_speaking_records(recordsToShow, startIndex);
    updatePaginationSpeaking(pageNumber, speakingRecords.length);


}

function showPageWriting(pageNumber) {
    const startIndex = (pageNumber - 1) * recordsPerPage;
    const endIndex = startIndex + recordsPerPage;
    const recordsToShow = writingRecords.slice(startIndex, endIndex);
    add_writing_records(recordsToShow, startIndex);
    updatePaginationWriting(pageNumber, writingRecords.length);
}
/////////////////////////////
/// load paging functions ///
/////////////////////////////

showPageWriting(1);

showPageListening(1);

showPageReading(1);

showPageSpeaking(1);
////////////////////////
/// delete questions ///
////////////////////////
function delete_writing_question(id) {
    return new Promise((resolve, reject) => {
        $.ajax({
            url: '/teacher/deleteWritingQuestion',
            method: 'POST',
            headers: {
                "X-CSRFTOKEN": getCookie('csrftoken')
            },
            data: { id: id },
            success: (data) => {
                resolve(data);
            },
            error: (error) => {
                reject(error);
            }
        });
    });
}

function delete_reading_question(id) {
    return new Promise((resolve, reject) => {
        $.ajax({
            url: '/teacher/deleteReadingQuestion',
            method: 'POST',
            headers: {
                "X-CSRFTOKEN": getCookie('csrftoken')
            },
            data: { id: id },
            success: (data) => {
                resolve(data);
            },
            error: (error) => {
                reject(error);
            }
        });
    });
}

function delete_speaking_question(id) {
    return new Promise((resolve, reject) => {
        console.log(id)
        $.ajax({
            url: '/teacher/deleteSpeakingQuestion',
            method: 'POST',
            headers: {
                "X-CSRFTOKEN": getCookie('csrftoken')
            },
            data: { id: id },
            success: (data) => {
                resolve(data);
            },
            error: (error) => {
                reject(error);
            }
        });
    });
}

function delete_listening_question(id) {
    return new Promise((resolve, reject) => {
        $.ajax({
            url: '/teacher/deleteListeningQuestion',
            method: 'POST',
            headers: {
                "X-CSRFTOKEN": getCookie('csrftoken')
            },
            data: { id: id },
            success: (data) => {
                resolve(data);
            },
            error: (error) => {
                reject(error);
            }
        });
    });
}

//////////////////////////////
/// delete a single record ///
//////////////////////////////

function delete_single_writing_record(id) {
    message_dialog(delete_writing_question, id, 'Do you want to delete the question?', writingRecords, add_writing_records).then(function (response) {
        writingRecords = response
    });
}

function delete_single_reading_record(id) {
    message_dialog(delete_reading_question, id, 'Do you want to delete the question?', readingRecords, add_reading_records).then(function (response) {
        readingRecords = response
    });
}

function delete_single_speaking_record(id) {
    console.log('delete_single_speaking_record', id)
    message_dialog(delete_speaking_question, id, 'Do you want to delete the question?', speakingRecords, add_speaking_records).then(function (response) {
        speakingRecords = response
    });
}

function delete_single_listening_record(id) {
    message_dialog(delete_listening_question, id, 'Do you want to delete the question?', listeningRecords, add_listening_records).then(function (response) {
        listeningRecords = response
    });
}




