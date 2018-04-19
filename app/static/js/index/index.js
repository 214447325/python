/**
 * Created by User on 2018/3/9.
 */

$(function() {
    var $body = $('body');
    $.post('/news/newsInfo',{name:'newsInfo'},function(data) {
        var link = '<link rel="stylesheet" href="http://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.css">';
        var script = '<script src="http://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.js"></script>';
        $('head').append(link + script);
        if(data.code == 1) {
            var listData = data.data;
            var listHtml = '';
            listHtml += '<div data-role="header">';
            listHtml += '<h1>主页</h1>';
            listHtml += '<a href="#" class="ui-btn ui-btn-right ui-shadow ui-icon-refresh ui-btn-icon-right">刷新</a>';
            listHtml += '</div>';
            listHtml += '<div data-role="main" class="ui-content" >';
            for(var i = 0; i < listData.length; i++) {
                //newsDeleteId为0表示该帖子还未失效
                if(listData[i].newsDeleteId == 0) {
                    listHtml += '<div data-role="collapsible" newsId="' + listData[i].newsId + '">';
                    listHtml += '<h1>' + listData[i].newsName + '</h1>';
                    listHtml += '<p>' + listData[i].newsContent + '</p>';
                    listHtml += '</div>';
                }
            }
            listHtml += '</div>';
            listHtml += '<div data-role="footer" style="width:100%;position:fixed;bottom: 0;">';
            listHtml += '<div data-role="navbar">';
            listHtml += '<ul>';
            listHtml += '<li><a href="#" data-icon="home">主页</a></li>';
            listHtml += '<li><a href="#" data-icon="arrow-r">下一页</a></li>';
            listHtml += '<li><a href="user.html" data-icon="user" data-transition="flip" class="users">用户</a></li>';
            listHtml += '</ul>';
            listHtml += ' </div>';
            listHtml += '</div>';
            $('#pageone').html(listHtml);
            //点击刷新功能
            $('.ui-icon-refresh').click(function(){
                window.location.reload();
            });

        } else {
            alert(data.message);
            return false;
        }
    },'json');

});
