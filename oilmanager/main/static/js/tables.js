

function clearFilter() {
    const url = new URL(window.location.href);
    url.search = ''; // Clear query parameters
    window.location.href = url.href;
}