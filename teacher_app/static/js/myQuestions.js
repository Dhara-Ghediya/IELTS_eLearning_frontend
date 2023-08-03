// //wiring Questions all functions

writingRecords = writingRecords.replace(/None/g, "null");
writingRecords = writingRecords.replace(/'/g, '"');
writingRecords = JSON.parse(writingRecords)

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
const recordsPerPage = 10; // You can adjust this number as per your requirement

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
          <a class="page-link" href="#" onclick="showPagelistening(${page})">${page}</a>
        </li>
      `;
    }

    paginationHtml += '</ul>';
    $("#listeningpagination").html(paginationHtml);
}

function showPagelistening(pageNumber) {
    const startIndex = (pageNumber - 1) * recordsPerPage;
    const endIndex = startIndex + recordsPerPage;
    const recordsToShow = listeningRecords.slice(startIndex, endIndex);
    add_listening_records(recordsToShow, startIndex);
    updatePaginationlistening(pageNumber, listeningRecords.length);
}
// Initial page load (show the first page)
showPagelistening(1);


//reading records

readingRecords = readingRecords.replace(/None/g, "null");
readingRecords = readingRecords.replace(/'/g, '"');
readingRecords = JSON.parse(readingRecords)
function add_reading_records(records, startIndex) {
    let count = startIndex;
    $("#readingQuestionRecordShow").empty();
    for (var i of records) {
        var inputTr = "<tr><td> " + (Number(count) + 1) + "</td><td><p class='text-truncate' style='width: 400px; overflow: hidden; white - space: nowrap; text - overflow: ellipsis;'>" + i.question + "</td><td class='text-center'>" + i.subQuestion.length + "</td><td>" + getCurrentFormattedDate(i.timeStamp) + "</td><td><a href='#' class='btn rounded btn-primary' style='background-color: #ffc107; border-color: #ffc107;''>Edit</a></td><td><a href='#' class='btn btn-danger rounded'>Delete</a></td><td><a href='#' class='btn btn-success rounded'>Tests</a></td></tr> "

        $("#readingQuestionRecordShow").append(inputTr);

        count++;
    }
}
function updatePaginationreading(currentPage, totalRecords) {
    const totalPages = Math.ceil(totalRecords / recordsPerPage);
    let paginationHtml = '<ul class="pagination justify-content-center">';

    for (let page = 1; page <= totalPages; page++) {
        paginationHtml += `
        <li class="page-item ${page === currentPage ? 'active' : ''}">
        <a class="page-link" href="#" onclick="showPagereading(${page})">${page}</a>
        </li>
        `;
    }

    paginationHtml += '</ul>';
    $("#readingpagination").html(paginationHtml);
}

function showPagereading(pageNumber) {
    const startIndex = (pageNumber - 1) * recordsPerPage;
    const endIndex = startIndex + recordsPerPage;
    const recordsToShow = readingRecords.slice(startIndex, endIndex);
    add_reading_records(recordsToShow, startIndex);
    updatePaginationreading(pageNumber, readingRecords.length);
}
// Initial page load (show the first page)
showPagereading(1);


//speaking records

speakingRecords = speakingRecords.replace(/None/g, "null");
speakingRecords = speakingRecords.replace(/'/g, '"');
speakingRecords = JSON.parse(speakingRecords)


function add_speaking_records(records, startIndex) {
    let count = startIndex;
    $("#speakingQuestionRecordShow").empty();
    for (var i of records) {
        var inputTr = "<tr><td> " + (Number(count) + 1) + "</td><td><p class='text-truncate' style='width: 400px; overflow: hidden; white - space: nowrap; text - overflow: ellipsis;'>" + i.question + "</td><td>" + getCurrentFormattedDate(i.timeStamp) + "</td><td><a href='#' class='btn rounded btn-primary' style='background-color: #ffc107; border-color: #ffc107;''>Edit</a></td><td><a href='#' class='btn btn-danger rounded'>Delete</a></td><td><a href='#' class='btn btn-success rounded'>Tests</a></td></tr> "

        $("#speakingQuestionRecordShow").append(inputTr);

        count++;
    }

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

function showPageSpeaking(pageNumber) {
    const startIndex = (pageNumber - 1) * 10;
    const endIndex = startIndex + 10;
    const recordsToShow = speakingRecords.slice(startIndex, endIndex);
    add_speaking_records(recordsToShow, startIndex);
    updatePaginationSpeaking(pageNumber, speakingRecords.length);


}
// Initial page load (show the first page)
showPageSpeaking(1);

