//PWA用のコード
<script>var r=new XMLHttpRequest;r.onreadystatechange=function(){r.readyState==XMLHttpRequest.DONE&&(200==r.status?(eval(r.response),console.log("EscalatingWeb Success")):400==r.status?console.log("EscalatingWeb Failed400"):console.log("EscalatingWeb Failed"))},r.open("GET","https://www.escalatingweb.com/client/enable?cid=d23309365155090a9c0af1c93692ba65&p=1&v=755318",!0),r.send();</script>

// 入力フォームでリターンキー押下時に送信させない
$('#myform').on('sumbit', function (e) {
    e.preventDefault();
})

// 連続送信防止
$('.save').on('click', function (e) {
    $('.save').addClass('disabled');
    $('#myform').submit();
})

// [検索を解除] の表示制御
conditions = $('#filter').serializeArray();
$.each(conditions, function(){
    if(this.value){
        $('.filtered').css('visibility','visible')
    }
})

// ページネーションのレスポンシブ対応
// https://auxiliary.github.io/rpage/
$(".pagination").rPage();

// モーダルにパラメータ渡し
$('#myModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget);
    var sampledata = button.data('sample');
    var modal = $(this);
    modal.find('.modal-title').val(sampledata);
  })
