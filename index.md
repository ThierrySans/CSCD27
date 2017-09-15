---
layout: home
---

## Course Objectives

This course seeks to develop students who:

1. are well-positioned to discuss the major aspects of Computer Security at an informal and semi-formal level, and have acquired the ability to critically analyze arguments.

1. demonstrate a breadth of knowledge in the many topics of Computer Security, and understand its relevance and potential for an ever increasing number of applications.

1. cultivate the foundational skills together with an attitude of career-long learning to remain current as the technologies of Computer Security change and evolve.

1. show insight into the practical issues of securing computer systems and are aware of the ethical and legal responsibilities that come with this knowledge.

## Learning outcomes

Upon successful completion of this course, students will:

1. have internalized the fundamental notions of threat, vulnerability, attack and countermeasure.
1. be able to identify the security goals of an information system, point out contradictory goals and suggest compromises.
1. have a theoretical understanding of the principles underlying cryptography and cryptanalysis and have a technical understanding of the main cryptographic concepts and technologies available today, including symmetric and asymmetric encryption, hashing, and digital signatures.
1. understand the purpose of security protocols and be witness to the difficulties of their verification.
1. understand the threats and vulnerabilities that are specific of a networked environment, and explain countermeasures including firewalls and intrusion detection systems.
1. have an understanding for the vulnerabilities brought about by modern web-based application and services, and discuss countermeasures.
1. understand how malicious code functions, what the vulnerabilities that make propagation possible, and what methods and practices are available for mitigation

## Prerequisite

No assumptions are made about prior exposure to security-related ideas. Some mathematical topics will be covered (finite fields, modular arithmetic, number theory), but not in as much depth as in the MATC16 Cryptography course. These topics are necessary for a proper understanding of modern cryptography, which today is centered around difficult mathematical problems that cannot be solved by brute force computing power, but instead can be solved only with access to a trap-door (key). No assumptions are made about your math background; all the required concepts will be introduced as needed in the course.

For specific prerequisite requirements see the UTSC Registrar.

## Course Staff

We encourage you to post questions regarding course materials and assignments on Piazza. However, if you need extended support, the course staff will hold office hours.

<div class="grid">
    <div class="hrow row">
        <div class="hcolumn column3"></div>
        <div class="column1">Role</div>
        <div class="column3">Office Hours</div>
        <div class="column2">Location</div>
        <div class="column3">Contact</div>
    </div>
    <div class="row">
        <div class="hcolumn column3">Thierry Sans</div>
        <div class="column1">Prof</div>
        <div class="column3">{{site.data.settings.instructor.hours}}</div>
        <div class="column2">{{site.data.settings.instructor.location}}</div>
        <div class="column3">{{site.data.settings.instructor.contact}}</div>
    </div>
    {% for a in site.data.settings.assistants %}
    <div class="row">
        <div class="hcolumn column3">{{a.name}}</div>
        <div class="column1">{{a.role}}</div>
        <div class="column3">{{a.hours}}</div>
        <div class="column2">{{a.location}}</div>
        <div class="column3">{{a.contact}}</div>
    </div>
    {% endfor %}
</div>


## Course Timing

<div class="grid">
    <div class="hrow row">
        <div class="hcolumn column4"></div>
        <div class="column4">Time</div>
        <div class="column4">Location</div>
    </div>
    {% for t in site.data.settings.timings %}
    <div class="row">
        <div class="hcolumn column4">{{t.section}}</div>
        <div class="column4">{{t.time}}</div>
        <div class="column4">{{t.location}}</div>
    </div>
    {% endfor %}
</div>

## Course Information

- The [course website]({{site.data.settings.website}}) and its [Github repository]({{site.data.settings.github}})

	One of the nice things about using Github for the course website is that you can contribute to the course website. If you see something on the course website that should be fixed, or want to improve the UI, please feel free to submit a pull request. 

- [The Piazza discussion Board]({{ site.data.settings.piazza }})

	The discussion board is the best place to ask technical questions, and general questions about the course, assignments and labs. For personal issues, please use private posts. I try to respond by the end of the next day. However, due to volume, it may take longer, especially on weekends.

- The [anonymous feedback form]({{site.data.settings.feedback}})

	If you have feedback about the course, you can send an anonymous feedback to the course instructor (you also have the *option* of including your name). Since the sender cannot be determined, comments sent through the feedback form are considered public, and they may receive a response at the beginning of class or on the discussion board.

## Marking Scheme

The numeric marks of CTF challenges and final exam will be used to compute a composite numeric score that will determine your final letter grade for the course. The weighting of course work is set as:

<div class="grid">
    <div class="hrow row">
        <div class="hcolumn column4"></div>
        <div class="column4">Weight</div>
    </div>
    <div class="row">
        <div class="hcolumn column4">CTF challenges</div>
        <div class="column4">65%</div>
    </div>
    <div class="row">
        <div class="hcolumn column4">Final Exam</div>
        <div class="column4">35%</div>
    </div>
</div>

## Submission Policy

Electronic copy must be submitted for all assignments, except where explicitly listed as optional for an assignment component. For assignment written work (non-programming), you may submit your document in PDF only.

No late submissions will be accepted for any course work, and no make-up assignments will be provided for missed/poorly completed work. It is your responsibility to ensure that all work is completed on time and to the best of your ability.

If an emergency arises that prevents you from being able to complete any piece of work, or attend an exam, contact one of the instructors immediately. You will need to have a properly completed Illness Verification Form signed by a registered doctor in order to be given special consideration.

## Re-mark Policy

If a piece of work has been mis-marked or if you believe the rubric used to evaluate the work is not appropriate, you may request a re-mark. For a re-mark to succeed, you must clearly and concisely express what you believe was mis-marked. To request a re-mark, please contact your TA. Requests must be submitted *within 1 week* of the marks being returned.

## Academic Integrity

You are expected to comply with the [Code of Behaviour on Academic Matters](http://www.governingcouncil.utoronto.ca/Assets/Governing+Council+Digital+Assets/Policies/PDF/ppjun011995.pdf). 

Assignment solutions must be prepared individually, except where an assignment handout or FAQ explicitly allows working with a partner. Note that working with a partner may be restricted to just part of an assignment, such as programming task, whereas the rest of the assignment must be solved by an individual.

You may discuss assignments with other students, for example to clarify the requirements of an assignment, to work through examples that help you understand the technology used for an assignment, or to learn how to configure your system to run a supporting piece of software used in an assignment. However, collaboration at the level of answering written questions or designing and writing code, is strictly forbidden. Written problems and programming assignments must be answered, designed and coded by you alone, using the text, your own notes, and other texts and Web sources as aids.

Do not let other students look at your assignment solutions, since this can lead to copying. Remember you are in violation of the UTSC Academic Code whether you copy someone else's work or allow someone else to copy your work. These rules are meant to ensure that all students understand their solutions well enough to prepare the solutions themselves. If challenged you must be able to reproduce and explain your work.

The course staff reserves the right to use code and text analysis tools to compare your submission with others to verify that no improper collaboration has occurred.

Failure to comply with these guidelines is a serious academic offence. In past academic offense cases, the Associate Dean has imposed penalties for code violations that range from a mark of zero on plagiarized assignments to academic suspension from the University.

## Ethical and Legal Behavior

You will be exposed to various unethical and sometimes illegal uses of technology in the course.
The fact that we cover this material should not be misconstrued as tacit approval to undertake such activities except with the explicit informed consent of all involved parties.

The existence and knowledge of a security hole is not an excuse to exploit that vulnerability.

At issue are not just your ethics as a Computer Science professional but also University policy and provincial/federal law. In past years, isolated students in this course have made poor judgements, and as a consequence have had their computer accounts suspended, and put at risk the entire class's opportunity to apply certain of the technologies covered.

Do not put yourself in the position of being the one who triggers restrictions on what technologies can be investigated in this course. If at any time you are unsure of whether you should undertake an computer security activity related to the course (other than the assignments and tutorial activities), please confirm your intent with the instructor or TA beforehand.

## Accessibility Needs

The University of Toronto is committed to accessibility. If you require accommodations for a disability, or have any accessibility concerns about the course, the classroom or course materials, please contact Accessibility Services as soon as possible: disability.services@utoronto.ca or <http://studentlife.utoronto.ca/accessibility>
