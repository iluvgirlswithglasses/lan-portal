
// for each 'download-all' button as `e`
Array.prototype.forEach.call(document.getElementsByClassName("dl-all-bt"), (e) => {
	e.addEventListener("click", (ev) => {
		let dl = ev.target.getAttribute("data");
		// for each 'download' button that is in `dl` directory
		Array.prototype.forEach.call(document.getElementsByClassName(dl), (d) => {
			d.click()
		});
	});
});
