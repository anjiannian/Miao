function load_week_time(){
    //TODO : test
    var free_time = eval($("#id_free_time").val());
    var morning_list = free_time["morning"];
    var afternoon_list = free_time["afternoon"];

    for(i in morning_list){

    }
    $("#id_morning td").each(function(){
        var select_td = $(this);
        for(i in morning_list){
            if(select_td.attr("id").substring(5,6) == i){
                select_td.css("background-color", "red").text("O");
            }
        }
    });
    $("#id_afternoon td").each(function(){
        var select_td = $(this);
        for(i in afternoon_list){
            if(select_td.attr("id").substring(5,6) == i){
                select_td.css("background-color", "red").text("O");
            }
        }
    });

}

function submit_apply(){
    $("#id_free_time").val(JSON.stringify(get_selected_time()));
    $("#apply_form").submit();
}


function get_selected_time(){
    var morning_list = [];
    var afternoon_list = [];
    $("#id_morning td").each(function(){
        var select_td = $(this);
        if(select_td.text() == 'O'){
            morning_list[morning_list.length] = select_td.attr("id").substring(5,6);
        }
    });
    $("#id_afternoon td").each(function(){
        var select_td = $(this);
        if(select_td.text() == 'O'){
            afternoon_list[afternoon_list.length] = select_td.attr("id").substring(5,6);
        }
    });

    return {
        "morning": morning_list,
        "afternoon": afternoon_list
    }
}
