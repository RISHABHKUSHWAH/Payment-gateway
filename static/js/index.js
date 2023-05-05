function getServices() {
    if ($("#service-dropdrown").hasClass('close')) {
        $("#service-dropdrown").removeClass("hide");
        $("#service-dropdrown").addClass("open");
        $("#service-dropdrown").removeClass("close");
    } else {
        $("#service-dropdrown").removeClass("open");
        $("#service-dropdrown").addClass("hide");
        $("#service-dropdrown").addClass("close");
    }
}
function getList() {
    if ($("#service-list").hasClass('close')) {
        $("#service-list").removeClass("hide");
        $("#service-list").addClass("open");
        $("#service-list").removeClass("close");
    } else {
        $("#service-list").removeClass("open");
        $("#service-list").addClass("hide");
        $("#service-list").addClass("close");
    }
}
