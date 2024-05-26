fig.add_shape(type='line', x0=size_class_growth['Size Class'].iloc[0], y0=average_growth,
                          x1=size_class_growth['Size Class'].iloc[-1], y1=average_growth,
                          line=dict(color="black", width=1, dash='dash'))