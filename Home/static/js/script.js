//Chức năng nút đi lên đầu trang
function goToTop() {
    const duration = 500;
    const start = window.scrollY;
    const startTime = performance.now();

    function easeInOutQuad(t, b, c, d) {
        t /= d / 2;
        if (t < 1) return (c / 2) * t * t + b;
        t--;
        return (-c / 2) * (t * (t - 2) - 1) + b;
    }

    function scroll() {
        const currentTime = performance.now();
        const time = Math.min(1, (currentTime - startTime) / duration);
        const newPosition = easeInOutQuad(time, start, -start, 1);
        window.scroll(0, newPosition);

        if (time < 1) {
            requestAnimationFrame(scroll);
        }
    }

    requestAnimationFrame(scroll);
}

window.onscroll = function() {
    const button = document.getElementById('go_up');
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        button.style.display = 'block';
    } else {
        button.style.display = 'none';
    }
};


//Popover
var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
  var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
    return new bootstrap.Popover(popoverTriggerEl)
  })


//Tooltip
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})

//cảm xúc của feedback
document.addEventListener('DOMContentLoaded', function () {
    // Lấy trạng thái màu từ localStorage
    const savedColor = localStorage.getItem('selectedColor');

    // Nếu có trạng thái màu, áp dụng nó
    if (savedColor) {
        document.querySelectorAll('.emotion').forEach(function (icon) {
            icon.classList.remove('selected');
            if (icon.getAttribute('data-emotion') === savedColor) {
                icon.classList.add('selected');
            }
        });
    }

    // Thêm sự kiện click cho mỗi thẻ <i>
    document.querySelectorAll('.emotion').forEach(function (icon) {
        icon.addEventListener('click', function () {
            // Lưu trạng thái màu vào localStorage
            localStorage.setItem('selectedColor', icon.getAttribute('data-emotion'));

            // Xóa trạng thái màu từ tất cả các thẻ <i>
            document.querySelectorAll('.emotion').forEach(function (otherIcon) {
                otherIcon.classList.remove('selected');
            });

            // Thêm trạng thái màu cho thẻ <i> được click
            icon.classList.add('selected');
        });
    });
});

//
const savedNewColor = localStorage.getItem('selectedNewColor');
if (savedNewColor) {
    document.querySelectorAll('.new-emotion').forEach(function (div) {
        div.classList.remove('background-selected');
        if (div.getAttribute('data-new-emotion') === savedNewColor) {
            div.classList.add('background-selected');
        }
    });
}

// Thêm sự kiện click cho new-emotions
document.querySelectorAll('.new-emotion').forEach(function (div) {
    div.addEventListener('click', function () {
        localStorage.setItem('selectedNewColor', div.getAttribute('data-new-emotion'));
        document.querySelectorAll('.new-emotion').forEach(function (otherDiv) {
            otherDiv.classList.remove('background-selected');
        });
        div.classList.add('background-selected');
    });
});

//script cho select (home)

