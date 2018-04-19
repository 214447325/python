/**
 * Created by User on 2018/3/16.
 */
$(function() {

    var userId = sessionStorage.getItem('userId');
    if(userId == undefined || userId == null || userId == '') {
        var users_html = '';
        users_html += '<div class="user_div1">';
        users_html += '<div class="user_div1_button1"><button class="user_div1_login">登录</button></div>';
        users_html += '<div class="user_div1_button2"><button class="user_div1_registe">注册</button></div>';
        users_html += '</div>';
        var u_html = '';
        u_html += '<form name="userForm" class="user_registe_form" style="display: none;">';
        u_html += '<div class="ui-field-contain">';
        u_html += '<label for="user">姓名：</label>';
        u_html += '<input type="text" name="user" id="user" placeholder="请输入姓名" value="">';
        u_html += '<label for="bday">生日：</label>';
        u_html += '<input type="date" name="bday" id="bday">';
        u_html += '<label for="phone">手机号:</label>';
        u_html += '<input type="text" name="phone" id="phone" placeholder="请输入手机号">';
        u_html += '<label for="password">密码：</label>';
        u_html += '<input type="password" name="password" id="password" placeholder="请输入密码">';
        u_html += '</div>';
        u_html += '<input type="button" data-inline="true" class="user_form_submit" value="提交">';
        u_html += '<input type="reset" data-inline="true" value="重置">';
        u_html += '</form>';
       $('.ui-content').html(users_html + u_html);
        //点击注册
        $('.user_div1_registe').click(function() {
            $('.user_registe_form').show();
        });

        //点击注册提交
        $('.user_form_submit').click(function() {
            var map = {};
            var name_value = $('#user').val().trim();
            var bday_value = $('#bday').val().trim();
            var phone_value = $('#phone').val().trim();
            var password_value = $('#password').val().trim();
            //if(name_value != undefined && name_value != null && name_value != '') {
            //    map.userName = name_value;
            //} else {
            //    alert('请输入用户名！');
            //    return false;
            //}
            //if(bday_value != undefined && bday_value != null && bday_value != '') {
            //    map.birthday = bday_value;
            //} else {
            //    alert('请选择用户生日！');
            //    return false;
            //}
            //if(phone_value != undefined && phone_value != null && phone_value != '') {
            //    map.phone = phone_value;
            //} else {
            //    alert('请输入用户名！');
            //    return false;
            //}
            //if(password_value != undefined && password_value != null && password_value != '') {
            //    map.password = password_value;
            //} else {
            //    alert('请输入密码！');
            //    return false;
            //}
            map = {name:'addUser',"userName":"陈东","birthday":"2018-03-02","phone":"15189854880","password":"111"};
            //var array = [map];
            $.post('/users/addUser',map,function() {

            },'json')
        })
    }

    var link = '<link rel="stylesheet" href="http://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.css">';
    var script = '<script src="http://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.js"></script>'
    $('head').append(link + script);
});