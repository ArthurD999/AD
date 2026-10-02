function display_hello_btn(){
alert('Crazy surprise! :)' );
}

function update_user_name_btn(){
//get the value from the user input
let user_name_input = document.getElementById('user_name').value;
//update the span tag with the user input
document.getElementById('user_name_place_holder').innerHTML =
user_name_input;
}


function calculate_mean(){
//Get the user data
let data_from_user = document.getElementById('user_dataset_1').value;
//split string data_from_user to list
let data_in_list = data_from_user.split(',')
//set up our variables
let total = 0
let num_items = 0
//iterate through the list to get the total
for (let temp of data_in_list){
//input is text so we need to cast to float
total = total + parseFloat(temp);
}
//get the number of items in the list
num_items = data_in_list.length;
//calculate the average
let average = total/num_items
return average
}
function calculate_mean_btn(){
document.getElementById('mean_placeholder').innerHTML =
calculate_mean();
}
function calculate_median(){
//Get the user data
let data_from_user = document.getElementById('user_dataset_1').value;
//split string data_from_user to list
let data_in_list = data_from_user.split(',')
//sort the list in ascending order
data_in_list.sort((a, b) => parseFloat(a) - parseFloat(b));
//get the number of items in the list
let num_items = data_in_list.length;
let median;
if (num_items % 2 === 0) {
    // If even number of items, take the average of the two middle items
    let mid1 = parseFloat(data_in_list[num_items / 2 - 1]);
    let mid2 = parseFloat(data_in_list[num_items / 2]);
    median = (mid1 + mid2) / 2;
} else {
    // If odd number of items, take the middle item
    median = parseFloat(data_in_list[Math.floor(num_items / 2)]);
}
return median;
}
function calculate_range(){
//Get the user data
let data_from_user = document.getElementById('user_dataset_1').value;
//split string data_from_user to list
let data_in_list = data_from_user.split(',')
//sort the list in ascending order
data_in_list.sort((a, b) => parseFloat(a) - parseFloat(b));
//calculate the range
let range = parseFloat(data_in_list[data_in_list.length - 1]) - parseFloat(data_in_list[0]);
return range;
}
function calculate_median_btn(){
document.getElementById('median_placeholder').innerHTML =
calculate_median();
}
function calculate_range_btn(){
document.getElementById('range_placeholder').innerHTML =
calculate_range();
}
function calculate_mode(){
//Get the user data
let data_from_user = document.getElementById('user_dataset_1').value;
//split string data_from_user to list
let data_in_list = data_from_user.split(',')
//count the frequency of each item
let frequency = {};
for (let item of data_in_list) {
    frequency[item] = (frequency[item] || 0) + 1;
}
//find the item with the highest frequency
let max_frequency = 0;
let mode = null;
for (let item in frequency) {
    if (frequency[item] > max_frequency) {
        max_frequency = frequency[item];
        mode = item;
    }
}
return mode;
}
function calculate_mode_btn(){
document.getElementById('mode_placeholder').innerHTML =
calculate_mode();
}
function calculate_frequency(){
//Get the user data
let data_from_user = document.getElementById('user_dataset_1').value;
//split string data_from_user to list
let data_in_list = data_from_user.split(',')
//count the frequency of each item
let frequency = {};
for (let item of data_in_list) {
    frequency[item] = (frequency[item] || 0) + 1;
}
return frequency;
}
function calculate_frequency_btn(){
let frequency = calculate_frequency();
let frequency_str = '';
for (let item in frequency) {
    frequency_str += `${item}: ${frequency[item]}<br>`;
}
document.getElementById('frequency_placeholder').innerHTML = frequency_str;
}