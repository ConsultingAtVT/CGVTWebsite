$(document).ready(function() {

  requestAnimationFrame(function() {
    var followingNavRef = $('.following.bar');
    var accountLinkRef = $('.account-link');
    var accountSidebarRef = $('#account-sidebar');
    var mobileMenuSidebarRef = $('#mobile-menu-sidebar');
    var mobileMenuBtnRef = $('#mobile-menu-btn');
    $('body')
      .visibility({
        offset: -1,
        observeChanges: false,
        once: false,
        continuous: false,
        onTopPassed: function() {
          requestAnimationFrame(function() {
            followingNavRef.addClass('scrolling');
          });
        },
        onTopPassedReverse: function() {
          requestAnimationFrame(function() {
            followingNavRef.removeClass('scrolling');
          });
        }
      });

    accountSidebarRef.sidebar('setting', {
      transition: 'right overlay',
      dimPage: false
    });

    accountLinkRef.on('click', function() {
      accountSidebarRef.sidebar('toggle');
    });

    mobileMenuSidebarRef.sidebar('setting', {
      transition: 'left overlay',
      dimPage: false
    });

    mobileMenuBtnRef.on('click', function() {
      mobileMenuSidebarRef.sidebar('toggle');
    });
  });

  requestAnimationFrame(function() {
    // these are popups that should show immediately
    var shownPopupElementRefs = $('.shown-popup-element');
    shownPopupElementRefs.popup({
      inline: true,
      on: 'click',
      onHide: function() {
        shownPopupElementRefs.popup('destroy');
      }
    }).popup('show');

    // these are popups that should show on hover
    var hoverPopupElementRefs = $('.hover-popup-element');
    hoverPopupElementRefs.popup({
      inline: true,
      on: 'hover'
    });
  });

});
