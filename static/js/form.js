layui.use(['form','element'], function(){
    var form = layui.form;
    var element = layui.element;
    //监听提交
    form.on('submit(formDemo)', function(data){
        layer.msg(JSON.stringify(data.field));
        return false;
    });

    form.on('submit(AddAgentForm)', function(data){
        layer.msg(JSON.stringify(data.field));
        return true;
    });

    form.on('submit(QueryAgentForm)', function(data){
        layer.msg(JSON.stringify(data.field));
        return true;
    });

});
