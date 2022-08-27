


path('lettings/', views.lettings_index, name='lettings_index'),
path('lettings/<int:letting_id>/', views.letting, name='letting'),
    