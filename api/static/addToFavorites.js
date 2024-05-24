// favorite.js
function addToFavorites() {
            // 尝试使用浏览器的API添加书签
            if (window.sidebar && window.sidebar.addPanel) { // For older Firefox
                window.sidebar.addPanel(document.title, window.location.href, '');
            } else if (window.external && ('addFavorite' in window.external)) { // IE
                window.external.addFavorite(window.location.href, document.title);
            } else if (window.opera && window.print) { // Opera
                var elem = document.createElement('a');
                elem.setAttribute('href', window.location.href);
                elem.setAttribute('title', document.title);
                elem.setAttribute('rel', 'sidebar'); // 用于兼容一些老版本Opera
                elem.click();
            } else { // Modern browsers, use the bookmark API
                alert('请按Ctrl+D键进行收藏！');
            }
        }