import grpc

import course_service_pb2
import course_service_pb2_grpc

# Устанавливаем соединение с сервером
channel = grpc.insecure_channel('localhost:50051')
stub = course_service_pb2_grpc.CourseServiceStub(channel)

# Отправляем запрос
response = stub.GetCourse(course_service_pb2.GetCourseResponse(course_id="cee626e7-972e-4cba-907f-ca32b62d16e0"))
print(response.course_id, response.title, response.description, sep='\n')  # Выведет: cee626e7-972e-4cba-907f-ca32b62d16e0 Автотесты API Будем изучать написание API автотестов
