from django.urls import path

from .views import (BBLoginView, BBLogoutView, BBPasswordChangeView,
                    BBPasswordResetCompleteView, BBPasswordResetConfirmView,
                    BBPasswordResetDoneView, BBPasswordResetView,
                    ChangeUserInfoView, DeleteUserView, RegisterDoneView,
                    RegisterUserView, by_rubric, detail, index, other_page,
                    profile, profile_bb_add, profile_bb_detail, user_activate)

app_name = 'main'
urlpatterns = [
    path(
        'accounts/register/activate/<str:sign>/',
        user_activate,
        name='register_activate'
    ),
    path(
        'accounts/register/done/',
        RegisterDoneView.as_view(),
        name='register_done'
    ),
    path(
        'accounts/register/',
        RegisterUserView.as_view(),
        name='register'
    ),
    path(
        'accounts/login/',
        BBLoginView.as_view(),
        name='login'
    ),
    path(
        'accounts/logout/',
        BBLogoutView.as_view(),
        name='logout'
    ),
    path(
        'accounts/password/change/',
        BBPasswordChangeView.as_view(),
        name='password_change'
    ),
    path(
        'accounts/password/reset/done/',
        BBPasswordResetDoneView.as_view(),
        name='password_reset_done'
    ),
    path(
        'accounts/password/reset/',
        BBPasswordResetView.as_view(),
        name='password_reset'
    ),
    path(
        'accounts/password/confirm/complete/',
        BBPasswordResetCompleteView.as_view(),
        name='password_reset_complete'
    ),
    path(
        'accounts/password/confirm/<uidb64>/<token>/',
        BBPasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
    path(
        'accounts/profile/change/',
        ChangeUserInfoView.as_view(),
        name='profile_change'
    ),
    path(
        'accounts/profile/delete/',
        DeleteUserView.as_view(),
        name='profile_delete'
    ),
    path(
        'accounts/profile/add/',
        profile_bb_add,  # type: ignore
        name='profile_bb_add'
    ),
    path(
        'accounts/profile/<int:pk>/',
        profile_bb_detail,
        name='profile_bb_detail'
    ),
    path(
        'accounts/profile/',
        profile,
        name='profile'
    ),
    path(
        '<int:rubric_pk>/<int:pk>/',
        detail,
        name='detail'
    ),
    path(
        '<int:pk>/',
        by_rubric,  # type: ignore
        name='by_rubric'
    ),
    path(
        '<str:page>/',
        other_page,
        name='other'
    ),
    path('', index, name='index'),
]
