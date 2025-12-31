from abc import ABC,abstractmethod
"""
Properties of Abstract class
Defined using abc module
    created using abc module
    from abc import ABC,abstract method
1.Cannot be instained :
    You can't create an object of an abstract class directly
    it acts as blue print for other classes

    from abc import ABC,abstractmethod

    class Shape(ABC):
    @abstractmethod
        def area(self):
            pass
    s = Shape() -> error can't instantize abstract class

2.Can contain abstract and concrete methods :
    Abstract : are declared but not implemented
    Concrete : can also exist and provide common functionality to subclass

    class Shape(ABC):
        @abstractmethod 
        def area(self):
            pass
        def display(self):
            print("THis is a shape)

3.Must be inherited:
    to use abstract class it must be inherited and implement all abstract methods in class
    class Circle(Shape):
       def area(self):
            return 3.14 *r*r
4.All abstract methods must be overriden :
    any subclass that does not implement all abstract methoda also become an abstract class and cannot be instantized
5.Support multiple inheritance:
    an abstract class can inherit from multiple classes including other abstract ones
    class A():
    class B(A):
    class C(A.B);
6.provide interface like behaviour:
    Abstract classes help in defining common interface for a gp of subclasses
    Enforces method consistency across all subclasses           
7.Helps in acheiving polymorphism:
    abstract class enable runtime polymorphoism ,allowing you to call the same method on different objects that share a common abstract base
            """
class MediaPlayer(ABC):
    def playAudio(self):
        print("can play audio\n")
    @abstractmethod
    def playVideo(self):
        pass
class SoundRecorder(MediaPlayer):
    def playVideo(self):
        print("can't play video\n")
class Vlcplayer(MediaPlayer):
    def playVideo(self):
        print("can play video\n")
sr = SoundRecorder()
sr.playAudio()
sr.playVideo()

vlc = Vlcplayer()
vlc.playAudio()
vlc.playVideo()

# x = MediaPlayer()
# x.playAideo() #== error